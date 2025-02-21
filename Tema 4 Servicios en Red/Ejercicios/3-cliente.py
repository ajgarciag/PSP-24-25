import socket

HOST = '127.0.0.1' 
PORT = 2000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.connect((HOST, PORT))
        print('✅ Conectado con éxito al servidor.')

        mensaje = s.recv(1024).decode('utf-8')
        print(f"🔹 {mensaje}")

        while True:
            letra = input(" Introduce una letra: ").strip()

            # Validar que solo se envíe una letra
            if len(letra) != 1 or not letra.isalpha():
                print(" Ingresa solo una letra válida.")
                continue

            s.send(letra.encode('utf-8'))
            respuesta = s.recv(1024).decode('utf-8')

            if respuesta == "Fin":
                mensaje = s.recv(1024).decode('utf-8')
                print(f" {mensaje}")
                break
            elif "Lo siento" in respuesta:
                print(f" {respuesta}")
                break
            else:
                print(f"🔹 {respuesta}")

    except ConnectionRefusedError:
        print("❌ No se pudo conectar al servidor. Asegúrate de que está en ejecución.")
    except ConnectionResetError:
        print("❌ El servidor cerró la conexión.")
    except KeyboardInterrupt:
        print("\n❌ Conexión cerrada manualmente.")
    finally:
        print("👋 Desconectado del servidor.")
