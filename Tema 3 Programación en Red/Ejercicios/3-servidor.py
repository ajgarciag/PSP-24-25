import socket

HOST = ''  # todas las interfaces locales a la escucha
PORT = 2000        # Puerto de escucha

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.bind((HOST, PORT))
  s.listen()
  conn, addr = s.accept() #línea bloqueante
  with conn:
    print(f"Conexión exitosa con el cliente. IP ({addr[0]}) Puerto ({addr[1]})")
    suma = 0
    while True:
      data = conn.recv(1024) #línea bloqueante
      print("El servidor ha recibido un número")
      if data == b"0":
        break
      else: 
        data.decode('utf-8')
        data = int(data)
        suma += data
    conn.send(str(suma).encode('utf-8'))

print(f"La suma final es {suma}")