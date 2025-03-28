import socket

HOST, PORT = "localhost", 5000

def start_client():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.settimeout(10)
            init_msg = s.recv(1024).decode()
            print(init_msg)

            while True:
                message = input("Escribe un mensaje: ")
                if not message:
                    continue

                s.sendall(message.encode())

                if message.upper() == "DESCONEXION":
                    response = s.recv(1024).decode()
                    print(response)
                    break

                response = s.recv(1024).decode()
                if not response:
                    print("[-] El servidor ha cerrado la conexión.")
                    break

                print(response)
    except ConnectionResetError:
        print("[-] El servidor ha cerrado la conexión.")

    except ConnectionRefusedError:
        print(f"[-] No se pudo conectar al servidor en {HOST}:{PORT}")

    except KeyboardInterrupt:
        print("\n[x] Interrumpido por el usuario.")

    finally:
        print("[x] Cerrando conexión.")

if __name__ == "__main__":
    start_client()
