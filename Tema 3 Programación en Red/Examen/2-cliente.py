import socket

HOST = '127.0.0.1'  
PORT = 2000        


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print('Conectado con éxito')

    nombre_usuario = input("Introduce su nombre de usuario: ")
    s.send(nombre_usuario.encode("utf-8"))

    mensaje = s.recv(1024)
    if mensaje == b"Usuario no registrado":
        print(f"El servidor dice: {mensaje}")

    else:
        print(f"El servidor dice: {mensaje}")
        pw = input()
        s.send(pw.encode('utf-8'))
        mensaje_final = s.recv(1024)
        print(f"El servidor dice: {mensaje_final}")