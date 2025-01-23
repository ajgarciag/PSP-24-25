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
    
    seguir = True
    while seguir:
        
        #recibimos el mensaje
        mensaje = conn.recv(1024) #línea bloqueante
        
        #cambiamos de byte-string a string normal
        mensaje = mensaje.decode('utf-8')

        if mensaje == 'exit':
           seguir = False
           #conn.close()  #cerramos socket cliente
           print("Cerramos el cliente")
        else: 
            print(f"{mensaje}")
            conn.send(mensaje.encode('utf-8'))

  print("Se ha cerrado el cliente") #estamos fuera del with conn:



        
