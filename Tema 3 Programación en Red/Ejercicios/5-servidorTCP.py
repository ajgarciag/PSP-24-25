import socket

HOST = '127.0.0.1'  # loopback
PORT = 2000        # Puerto de escucha


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.bind((HOST, PORT)) #emparejo el socket con la direccion Host+Puerto
  s.listen()
  print(f"Servidor escuchando en {HOST}:{PORT}...")
  conn, addr = s.accept() #línea bloqueante
  with conn:
    print(f"Conexión exitosa con el cliente. IP ({addr[0]}) Puerto ({addr[1]})")
    
    vocales = 'aeiou'
    cadena = conn.recv(1024) #espero a que el cliente me mande la cadena

    cadena = cadena.decode('utf-8')

    numero = 0
    for vocal in vocales:
      
      numero += cadena.count(vocal)


    conn.send(b"En la cadena hay " + str(numero).encode('utf-8')+b" vocales")
  
  print(f"En la cadena habia {numero} vocales. Cerramos la conexion") #estamos fuera del with conn:



        
