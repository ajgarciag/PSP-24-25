'''
import socket

HOST = '127.0.0.1'  
PORT = 2000        


usuarios = [["usuario1","123"],["usuario2","12345"],["usuario3","hola"]] 
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Servidor esperando conexión...")
    conn, addr = s.accept()

    with conn:
        usuario = conn.recv(1024).decode('utf-8')
        existe = 0
        for i in range(len(usuarios)):
            if usuario == usuarios[i][0]:
                existe = 1
                conn.send(b"Nombre de usuario correcto. Introduzca su clave:")
                pw = conn.recv(1024).decode('utf-8')
                if pw == usuarios[i][1]:
                    conn.send(b"Autentificacion realizada con exito")
                else:
                    conn.send(b"Clave incorrecta para este usuario")
        if existe == 0:
            conn.send(b"Usuario no registrado")
'''

import socketserver

usuarios = [["usuario1","123"],["usuario2","12345"],["usuario3","hola"]] 

class miHandler(socketserver.BaseRequestHandler):
  #Clase para manejar las conexiones, se instancia una por cliente
  def handle(self):#medodo a sobreescribir para nuestro propio manejo
    #self.request se refiere al socket client conectado
    print (f"Se han conectado desde: {self.client_address[0]} [{self.client_address[1]}]")
    
    usuario = self.request.recv(1024).decode('utf-8')
    existe = 0
    for i in range(len(usuarios)):
        if usuario == usuarios[i][0]:
            existe = 1
            self.request.send(b"Nombre de usuario correcto. Introduzca su clave:")
            pw = self.request.recv(1024).decode('utf-8')
            if pw == usuarios[i][1]:
                self.request.send(b"Autentificacion realizada con exito")
            else:
                self.request.send(b"Clave incorrecta para este usuario")
    if existe == 0:
        self.request.send(b"Usuario no registrado")
    
      
if __name__ == "__main__":  
    HOST = '127.0.0.1' 
    PORT = 2000
  #instanciamos el socket servidor con la clase asociada de callback
    server = socketserver.TCPServer((HOST, PORT), miHandler)
    try:
       print(f"Servidor a la escucha en {HOST}:{PORT}")
       server.serve_forever()
    except KeyboardInterrupt:
       print ("servidor finalizado")