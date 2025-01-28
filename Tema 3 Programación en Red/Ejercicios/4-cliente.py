import socket

HOST = '127.0.0.1'  
PORT = 2000        
buffer_size = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print('Conectado con éxito')

    nombre = input("Introduce el nombre del archivo: ")
    s.sendall(nombre.encode('utf-8'))

    existe = s.recv(buffer_size)
    if existe == b"OK":
        #recibir el contenido del archivo
        texto = ''
        while True:
            print("El cliente espera para recibir datos...")
            datos = s.recv(buffer_size)
            if b"EOF" in datos:  #si llega la señal de fin de archivo
               
                texto += datos.replace(b"EOF", b"").decode('utf-8')
                print(f"En esta iteración se han recibido {len(datos)} bytes")
                break
            
            texto += datos.decode('utf-8')  #decodificar y acumular el texto
            
            print(f"En esta iteración se han recibido {len(datos)} bytes")
            
        print(f"El servidor nos ha mandado este texto: {texto}")
    else:
        print(f"Error: El servidor dice: {existe}")