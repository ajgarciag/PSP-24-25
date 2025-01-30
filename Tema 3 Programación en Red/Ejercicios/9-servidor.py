import socket, random
# _ _ _ _ _
HOST = '127.0.0.1'  
PORT = 2000

personas = [] # lista que almacena objetos de clase Persona 
class Persona:
    def __init__(self,nombre,tlf):
        self.nombre = nombre
        self.tlf = tlf
    
    def mostrar_informacion(self):
        return f"Informacion de la persona: Nombre: {self.nombre}, Telefono: {self.tlf}"

def crear_persona(nombre, tlf):
    nuevo = Persona(nombre, tlf)
    personas.append(nuevo)
    return f"Datos de {nombre} creados correctamente"

def menu(conn):
    while True:
        n = conn.recv(1024).decode('utf-8')

        if n == '1':
            nombre = conn.recv(1024).decode('utf-8')
            tlf = conn.recv(1024).decode('utf-8')
            mensaje = crear_persona(nombre, tlf)
            conn.send(mensaje.encode('utf-8'))
        elif n == '2':
            nombre = conn.recv(1024).decode('utf-8')
            mensaje = ''
            for persona in personas:
                if nombre == persona.nombre:
                    mensaje = persona.mostrar_informacion()
            if mensaje == '':
                mensaje = "Persona no registrada"
            conn.send(mensaje.encode('utf-8'))
        elif n == '3': #esto se puede mejorar: fragmentar envios
            mensaje = ''
            for persona in personas:
                mensaje = mensaje + persona.mostrar_informacion()+'\n'
            datos = conn.send(mensaje.encode('utf-8'))
            print(datos)
        else:

            conn.send(b"Finalizamos la conexion")
            break



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Servidor esperando conexión...")
    conn, addr = s.accept()

    with conn:
        menu(conn)





