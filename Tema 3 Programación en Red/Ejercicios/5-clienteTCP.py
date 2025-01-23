import socket

HOST = '127.0.0.1'  
PORT = 2000        

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.connect((HOST, PORT))
  print('Conectado con éxito')


  cadena = input("Introduce una cadena: ").encode('utf-8')


  s.send(cadena) #mandamos al servidor la cadena

  print("Esperando respuesta....")

  respuesta = s.recv(1024) 

  print(f"El servidor dice: {respuesta} ")

  

