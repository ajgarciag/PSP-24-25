import socketserver

class TCPSocketHandler(socketserver.BaseRequestHandler):
  #Clase para manejar las conexiones, se instancia una por cliente
  def handle(self):
    print (f"Se han conectado desde: {self.client_address[0]} [{self.client_address[1]}]")
    self.data = self.request.recv(128).strip()
    print("Datos recibidos: ", self.data)
    self.request.sendall(self.data.upper())

if __name__ == "__main__":  
  HOST, PORT = "", 2000
  # instanciamos el socket servidor con la clase asociada de callback
  server = socketserver.TCPServer((HOST, PORT), TCPSocketHandler)
  try:
    while True:
      server.handle_request() #esto dentro de un while true es como el serve_forever
  except KeyboardInterrupt:
    print ("servidor finalizado")