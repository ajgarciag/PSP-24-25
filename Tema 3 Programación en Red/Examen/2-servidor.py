#Servidor TCP de autentificación

import socket

HOST = '127.0.0.1'  
PORT = 2000        


usuarios = [["usuario1","123"],["usuario2","12345"],["usuario3","hola"]] 
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Servidor esperando conexión...")
    conn, addr = s.accept()

    with conn:
        usuario = conn.recv(1024).decode('utf-8')
        existe = 0
        for i in range(len(usuarios)):
            if usuario == usuarios[i][0]:
                existe = 1
                conn.send(b"Nombre de usuario correcto. Introduzca su clave:")
                pw = conn.recv(1024).decode('utf-8')
                if pw == usuarios[i][1]:
                    conn.send(b"Autentificacion realizada con exito")
                else:
                    conn.send(b"Clave incorrecta para este usuario")
        if existe == 0:
            conn.send(b"Usuario no registrado")
        

    







