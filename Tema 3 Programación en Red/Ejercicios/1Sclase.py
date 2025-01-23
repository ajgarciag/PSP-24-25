import socket

HOST = '127.0.0.1'  # loopback
PORT = 2000        # Puerto de escucha

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.bind((HOST, PORT))
  s.listen()
  print(f"Servidor escuchando en {HOST}:{PORT}...")
  conn, addr = s.accept() #línea bloqueante
  with conn:
    print(f"Conexión exitosa con el cliente. IP ({addr[0]}) Puerto ({addr[1]})")
    
    #recibimos el nombre
    nombre = conn.recv(1024) #línea bloqueante
    
    #cambiamos de byte-string a string normal
    nombre = nombre.decode('utf-8')
   
    print(f"El servidor ha recibido {nombre}")
    
    cadena = ("Buenos días, " + nombre).encode('utf-8')
    
    #print(f"Buenos días, {nombre}")
    
    conn.sendall(cadena)