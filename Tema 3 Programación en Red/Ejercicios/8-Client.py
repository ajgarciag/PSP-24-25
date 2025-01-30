import socket

HOST = '127.0.0.1'  
PORT = 2000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print('Conectado con éxito')

    mensaje = s.recv(1024).decode('utf-8')
    print(f"El servidor dice: {mensaje}")

    while True:
        letra = input("Introduce una letra: ")
        s.send(letra.encode('utf-8'))

        turno = s.recv(1024)

        if turno == b"Fin":
            mensaje = s.recv(1024).decode('utf-8')
            print(f"El servidor dice: {mensaje}")
            break
        else:
            print(turno)

