import socket

HOST = '127.0.0.1'  
PORT = 2000        

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
  print('Conectado con éxito')
  cadena = input("Introduce una cadena: ").encode('utf-8')


  s.sendto(cadena,((HOST,PORT))) #mandamos al servidor la cadena

  print("Esperando respuesta....")

  respuesta, serv_adrr = s.recvfrom(1024) 

  print(f"El servidor dice: {respuesta} ")

  

