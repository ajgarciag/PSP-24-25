import socket

HOST = '127.0.0.1'  
PORT = 2000        

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.connect((HOST, PORT))
  print('Conectado con éxito')
  

  while True:
    nombre = input("Introduce un mensaje ")

    #pasamos 'nombre' (string) a byte-string

    nombre = nombre.encode('utf-8')
    
    s.send(nombre)

    if nombre==b'exit':
       break
    else:
       vuelta = s.recv(1024) #recibimos el mensaje de vuelta
       print(f"Se ha recibido un mensaje del servidor: {vuelta}")
       
      
    