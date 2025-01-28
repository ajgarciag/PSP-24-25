import socket

HOST = '127.0.0.1'  
PORT = 2000        


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print('Conectado con éxito')

    jugada = input("Introduce tu jugada (piedra, papel, tijeras):  ")
    s.sendall(jugada.encode('utf-8'))

    print("Esperando resultado del servidor...")

    mensaje = s.recv(1024)

    print("Resultado: "+mensaje.decode('utf-8'))
