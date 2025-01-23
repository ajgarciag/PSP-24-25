import socket

HOST = '127.0.0.1'  # loopback
PORT = 2000        # Puerto de escucha


with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
  s.bind((HOST, PORT)) #emparejo el socket con la direccion Host+Puerto
  
  vocales = 'aeiou'
  cadena, adrr = s.recvfrom(1024) #espero a que el cliente me mande la cadena

  cadena = cadena.decode('utf-8')

  numero = 0
  for vocal in vocales:
    numero += cadena.count(vocal)

  s.sendto(b"En la cadena hay " + str(numero).encode('utf-8')+b" vocales", adrr)
  
  print(f"En la cadena habia {numero} vocales. Cerramos la conexion") #estamos fuera del with conn:



        
