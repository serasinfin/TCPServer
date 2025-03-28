import socketserver

HOST, PORT = "localhost", 5000

class ServerHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print("[+] Nueva conexión")
        try:
            self.request.sendall("Conexión establecida. Escribe 'DESCONEXION' para salir.\n".encode())
            while True:
                data = self.request.recv(1024).strip()
                if not data:
                    print(f"[-] {self.client_address} Desconectado")
                    break

                message = data.decode()
                if message.upper() == "DESCONEXION":
                    print(f"[x] Cerrando conexión con {self.client_address}")
                    break
                else:
                    self.request.sendall(message.upper().encode())

        except ConnectionError:
            print(f"[-] Error de conexión con {self.client_address}")

        finally:
            self.request.close()


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    allow_reuse_address = True
    daemon_threads = True

if __name__ == "__main__":
    with ThreadedTCPServer((HOST, PORT), ServerHandler) as server:
        print(f"[+] Servidor iniciado en {HOST}:{PORT}")
        server.serve_forever()
