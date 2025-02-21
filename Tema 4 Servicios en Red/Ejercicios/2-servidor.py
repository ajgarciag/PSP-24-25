import socketserver

HOST = ''  # Todas las interfaces locales a la escucha
PORT = 2000  # Puerto de escucha

class ManejoSuma(socketserver.BaseRequestHandler):
    def handle(self): #sobreescribo el metodo handle
        print(f"Conexión exitosa con el cliente. IP ({self.client_address[0]}) Puerto ({self.client_address[1]})")
        suma = 0
        while True:
            numero = self.request.recv(1024)
            print("El servidor ha recibido un número")
            if numero == b"0":
                break
            try:
                suma += int(numero.decode('utf-8'))
            except ValueError:
                print("Dato no válido recibido, ignorando...")
        
        self.request.send(str(suma).encode('utf-8'))
        print(f"La suma final es {suma}")

if __name__ == "__main__":
    with socketserver.TCPServer((HOST, PORT), ManejoSuma) as server:
        print(f"Servidor escuchando en el puerto {PORT}...")
        server.serve_forever()


'''
import socket
HOST = ''  # todas las interfaces locales a la escucha
PORT = 2000        # Puerto de escucha

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.bind((HOST, PORT))
  s.listen()
  conn, addr = s.accept() #línea bloqueante
  with conn:
    print(f"Conexión exitosa con el cliente. IP ({addr[0]}) Puerto ({addr[1]})")
    suma = 0
    while True:
      data = conn.recv(1024) #línea bloqueante
      print("El servidor ha recibido un número")
      if data == b"0":
        break
      else: 
        data.decode('utf-8')
        data = int(data)
        suma += data
    conn.send(str(suma).encode('utf-8'))

print(f"La suma final es {suma}")
'''

'''
import socketserver

class TCPSocketHandler(socketserver.BaseRequestHandler):
  #Clase para manejar las conexiones, se instancia una por cliente
  def handle(self):#medodo a sobreescribir para nuestro propio manejo
    #self.request se refiere al socket client conectado
    print (f"Se han conectado desde: {self.client_address[0]} [{self.client_address[1]}]")
    while True:
      self.data = self.request.recv(128).strip()
      print("Datos recibidos: ", self.data)
      self.request.sendall(self.data.upper()) #remitimos los mismos datos en mayúscula
      if self.data == b"":
        break
      if self.data ==b"#":
        raise KeyboardInterrupt

if __name__ == "__main__":  
    HOST, PORT = "", 2000
  #instanciamos el socket servidor con la clase asociada de callback
    server = socketserver.TCPServer((HOST, PORT), TCPSocketHandler)
  #activamos el servidor (ponemos a la espera de clientes)
  #podemos provocar una excepción con Ctrl-C
    try:
       server.serve_forever()
    except KeyboardInterrupt:
       print ("servidor finalizado")
'''