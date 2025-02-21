import socketserver

def contar_vocales(cadena):
    vocales = ['a','e','i','o','u']
    contador = 0
    for letra in cadena:
       if letra in vocales:
          contador += 1
             
    return f"En esta cadena hay {contador} vocales"


class UDPHandler(socketserver.BaseRequestHandler):
  #self.request es el par [datos,socketServidor] !!!
  #la dirección del cliente es self.client_address
  def handle(self):
    cadena = self.request[0].decode('utf-8')
    sock = self.request[1]
    print(" El cliente: {} envió:".format(self.client_address)) 
    print(cadena)
    mensaje = contar_vocales(cadena).encode('utf-8')
    sock.sendto(mensaje, self.client_address)#envío de datos al cliente


if __name__ == "__main__":
  HOST = '127.0.0.1'
  PORT = 2000
  with socketserver.UDPServer((HOST, PORT), UDPHandler) as server:
    # activamos el servidor (ponemos a la escucha)
    print(f"Servidor instanciado en {HOST}:{PORT}")
    try:
      server.serve_forever()
    except:
      print ("servidor finalizado")