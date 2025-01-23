import socket

HOST = '127.0.0.1'  
PORT = 2000        

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:

    while True:
        numero = input("Introduce un numero: ")

        s.sendto(numero.encode('utf-8'),(HOST,PORT))

        mensaje, serv_adrr = s.recvfrom(1024)

        if mensaje == b"Correcto!":
            print(f"El servidor dice: {mensaje}")
            break
        else: 
            print(f"El servidor dice: {mensaje}")

        
  

  

