import socket

HOST = '127.0.0.1'
PORT = 2000

#definir
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    #se puede observar que no hay conectar
    #enviar
    cadena = input("Introduce una cadena para contar las vocales: \n")
  
    sock.sendto(cadena.encode('utf-8'), (HOST, PORT))
  
    #recibir
    respuesta, serv_adrr = sock.recvfrom(1024)
    print(f"El servidor dice: {respuesta.decode('utf-8')}")