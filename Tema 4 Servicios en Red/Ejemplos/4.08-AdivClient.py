import socket

def cliente():
    HOST = '127.0.0.1'  # Dirección IP del servidor (localhost)
    PORT = 2000         # Puerto en el que escucha el servidor
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        mensaje = s.recv(64).decode()
        print(mensaje)  # Mensaje de bienvenida del servidor
        
        while True:
            numero = input("Ingresa un número entre 1 y 9: ")
            s.send(numero.encode())
            respuesta = s.recv(64).decode()
            print("Servidor: ", respuesta)
            
            if "HAS ACERTADO" in respuesta:
                break

if __name__ == "__main__":
    cliente()