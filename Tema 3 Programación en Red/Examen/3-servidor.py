import socket

HOST = '127.0.0.1'  
PORT = 2000 

class Cliente:
    def __init__(self,nombre,saldo):
        self.nombre = nombre
        self.saldo = saldo
    
    def ingresar(self, ingreso):
        if ingreso < 0:
            return "No se puede ingresar una cantidad negativa"
        else:
            self.saldo += ingreso
            return f"Ingreso realizado. El saldo ahora es {self.saldo}"

    def sacar_dinero(self, sacar):
        if sacar > self.saldo:
            return f"Saldo insuficiente. Tu saldo es {self.saldo}" 
        elif sacar<0:
            return "No se puede retirar una cantidad negativa"
        else:
            self.saldo -= sacar
            return f"Dinero retirado correctamente. El saldo ahora es {self.saldo}"

lista_clientes = [] #gloabl
def crear_cliente(nombre, saldo):
    global lista_clientes
    existe = ''
    for cliente in lista_clientes:
        if nombre == cliente.nombre:
            existe = 'si'
    if existe == 'si':
        return "No se puede registrar: ya existe este cliente"
    elif saldo < 0:
        return "No se puede registrar: saldo negativo"
    else:
        nuevo = Cliente(nombre, saldo)
        lista_clientes.append(nuevo)
        return "Cliente registrado correctamente"

def menu(conn):
    global lista_clientes
    n = conn.recv(1024).decode('utf-8')
    if n == '1':
        nombre = conn.recv(1024).decode('utf-8')
        saldo = conn.recv(1024).decode('utf-8')
        return crear_cliente(nombre,int(saldo))
    if n == '2':
        nombre = conn.recv(1024).decode('utf-8')
        ingreso = conn.recv(1024).decode('utf-8')
        actual = ''
        for cliente in lista_clientes:
            if cliente.nombre == nombre:
                actual = cliente
        if actual != '':
            return actual.ingresar(int(ingreso))
        else:
            return "Cliente no registrado"
    if n == '3':
        nombre = conn.recv(1024).decode('utf-8')
        retiro = conn.recv(1024).decode('utf-8')
        actual = ''
        for cliente in lista_clientes:
            if cliente.nombre == nombre:
                actual = cliente
        if actual != '':
            return actual.sacar_dinero(int(retiro))
        else:
            return "Cliente no registrado"
    if n == '4':
        return "exit"
    else:
        return "Numero no valido"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Servidor esperando conexión...")
    conn, addr = s.accept()
    with conn:
        while True:
            mensaje = menu(conn)
            if mensaje == "exit":
                conn.send("Saliendo de la aplicacion...".encode('utf-8'))
                break
            else:
                conn.send(mensaje.encode('utf-8'))
        


