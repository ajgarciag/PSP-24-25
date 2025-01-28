import socket
import random
HOST = '127.0.0.1'  
PORT = 2000        


def juego(mano1,mano2):
    if mano1==mano2:
        return 0
    elif (mano1=="piedra" and mano2=="tijeras") or (mano1=="tijeras" and mano2=="papel") or (mano1=="papel" and mano2=="piedra"):
        return 1
    else:
        return 2
    
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Servidor esperando conexión...")
    conn, addr = s.accept()
    
    jugada = ["piedra","papel","tijeras"]

    with conn:
        print(f"Conexión exitosa con {addr}")

        jugada_cliente = conn.recv(1024).decode('utf-8')

        jugada_servidor = jugada[random.randint(0,2)]

        if jugada_cliente not in jugada:
            conn.send(b"Partida anulada, introduce una jugada valida")
        else:
            resultado = juego(jugada_servidor,jugada_cliente)

            if resultado == 0:
                cadena = b"empate"
            elif resultado == 1:
                cadena = b"ha ganado el servidor"
            else:
                cadena = b"ha ganado el cliente"
            
            conn.send(b"El servidor ha sacado " +jugada_servidor.encode('utf-8')+ b", "+ cadena)





