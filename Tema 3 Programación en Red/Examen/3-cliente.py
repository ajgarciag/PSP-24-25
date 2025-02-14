import socket

HOST = '127.0.0.1'  
PORT = 2000        


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print('Conectado con éxito')

    while True:
        n = input("Introduce: \n1 Crear cliente \n2 Ingresar dinero \n3 Retirar dinero \n4 Salir\n")
        s.send((n.encode('utf-8')))
        if n=='1':
            nombre = input("Nombre de la cuenta: ")
            saldo_inicial = input("Saldo inicial: ")
            s.send(nombre.encode('utf-8'))
            s.send(saldo_inicial.encode('utf-8'))
            mensaje = s.recv(1024)
            print(f"El servidor dice: {mensaje}")

        if n=='2':
            nombre = input("Nombre de la cuenta: ")
            ingreso = input("Dinero a ingresar: ")
            s.send(nombre.encode('utf-8'))
            s.send(ingreso.encode('utf-8'))
            mensaje = s.recv(1024)
            print(f"El servidor dice: {mensaje}")
        if n=='3':
            nombre = input("Nombre de la cuenta: ")
            retiro = input("Dinero a retirar: ")
            s.send(nombre.encode('utf-8'))
            s.send(retiro.encode('utf-8'))
            mensaje = s.recv(1024)
            print(f"El servidor dice: {mensaje}")
        if n=='4':
            mensaje = s.recv(1024)
            print(f"El servidor dice: {mensaje}")
            break