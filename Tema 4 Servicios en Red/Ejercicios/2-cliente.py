import socket

HOST = '127.0.0.1'  
PORT = 2000        

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.connect((HOST, PORT))
  print('Conectado con éxito')
  seguir = True
  while seguir:
    n = input("Introduce un numero para mandarle al servidor: ")

    s.send(n.encode('utf-8'))
    if n =='0':
      seguir = False

  final = s.recv(1024)
  print(f"El servidor dice que la suma es {final}")
    
    
