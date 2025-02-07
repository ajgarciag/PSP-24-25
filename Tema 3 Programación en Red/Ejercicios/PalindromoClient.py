import socket

HOST = '127.0.0.1'  
PORT = 2000        

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
   print('Conectado con éxito')

   while True:
    cadena = input("Introduce una cadena para ver si es palindromo o 'exit' para terminar: ").encode('utf-8')
    s.sendto(cadena,((HOST,PORT))) #mandamos al servidor la cadena
    if cadena ==b'exit':
      respuesta, serv_adrr = s.recvfrom(1024) 
      print(f"El servidor dice: {respuesta} ")
      break
    else:
       respuesta, serv_adrr = s.recvfrom(1024) 
       print(f"El servidor dice: {respuesta} ")
      
    



  