import socket

HOST = '127.0.0.1'  
PORT = 2000        

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.connect((HOST, PORT))
  print('Conectado con éxito')
  
  nombre = input("Introduce un nombre: ")

  #pasamos 'nombre' (string) a byte-string

  nombre = nombre.encode('utf-8')
  
  
  s.send(nombre)
 
  #recibe el saludo
  saludo = s.recv(1024) #línea bloqueante

  print(f"El servidor ha dicho: {saludo.decode('utf-8')}")

