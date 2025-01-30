import socket

HOST = '127.0.0.1'  
PORT = 2000        


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print('Conectado con éxito')
    
    while True:
        n = input("Introduce: \n 1. Crear Persona \n 2. Mostrar información individual \n 3. Mostrar toda la información \n 4. Salir \n")
        s.send(n.encode('utf-8'))
        if n == '1':
            nombre = input("Introduce el nombre: ")
            tlf = input("introduce el telefono: ")
            s.send(nombre.encode('utf-8'))
            s.send(tlf.encode('utf-8'))
            mensaje = s.recv(1024)
            print(f"El servidor dice: {mensaje}")
        elif n =='2':
            nombre = input("Introduce el nombre: ")
            s.send(nombre.encode('utf-8'))
            mensaje = s.recv(1024)
            print(f"El servidor dice: {mensaje}")
        elif n == '3':
            mensaje = s.recv(1024)
            print(f"El servidor dice: {mensaje}")
        else: 
            break
    
    mensaje = s.recv(1024)
    print(f"El servidor dice: {mensaje}")