import socket
import os

HOST = '127.0.0.1'  
PORT = 2000        
buffer_size = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Esperando conexión...")
    conn, addr = s.accept() #se queda parado hasta la conexion
    with conn:
        print(f"Conexión exitosa con {addr}")
        while True:
            nombre = conn.recv(buffer_size)
            if not nombre:
                break
            print(f"Recibido: {nombre.decode('utf-8')}")
            
            if os.path.exists(nombre.decode('utf-8')):
                conn.sendall(b"OK")
                with open(nombre.decode('utf-8'), 'rb') as f:
                    while True:
                        datos = f.read(buffer_size)
                        if not datos: #b''
                            conn.sendall(b"EOF")
                            break
                        conn.sendall(datos)
                
                
                print("Archivo enviado correctamente.")
            else:
                conn.sendall(b"El archivo no existe")
                break
