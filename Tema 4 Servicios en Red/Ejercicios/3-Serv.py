import socket,random, threading

HOST = '127.0.0.1'  
PORT = 2000

lista = ['universo', 'ventana', 'puerta', 'montana',
'biblioteca', 'computadora', 'palabras', 'verde', 'manzana', 'estrella', 'marinero',
'elefante', 'mariposa', 'murcielago', 'camino', 'animal', 'farola', 'servidor', 'arquitecto',
'cucaracha','palacio','ordenador','presidente','comision','astronauta']
lock = threading.Lock() #definir el candado
game_over = False #variable global para indicar si ha finalizado el juego

def mostrar_jugada(palabra):
    mostrar = ''
    for i in range(len(palabra)):
        mostrar +=palabra[i]+" "
    return mostrar

def ahorcado(palabra,conn):
    global game_over
    intentos = 6

    jugada = ["_" for i in range(len(palabra))]
    
    conn.send(f"Palabra a adivinar: {mostrar_jugada(jugada)}".encode('utf-8'))

    while intentos > 0:
        try:
            letra = conn.recv(1024).decode('utf-8')
            with lock:
                if game_over:
                    conn.send(b"Lo siento! Otro jugador ha ganado")
                    conn.close()
            
            if letra in palabra:
                for i in range(len(palabra)):
                    if palabra[i] == letra:
                        jugada[i] = letra
                print(jugada)
                if "_" not in jugada:
                    with lock:
                        game_over = True
                    conn.send(b"Fin")
                    enviar = f"Has ganado! La palabra era {palabra}"
                    conn.send(enviar.encode('utf-8'))
                    break
                else:
                    conn.send(mostrar_jugada(jugada).encode('utf-8'))
            else: 
                intentos -= 1
                if intentos == 0:
                    conn.send(b"Fin")
                    enviar = f"Has perdido! La palabra era {palabra}"
                    conn.send(enviar.encode('utf-8'))
                else:
                    mensaje = f"La letra {letra} no esta en la palabra. Te quedan {intentos} intentos"
                    print(mensaje)
                    conn.send(mensaje.encode('utf-8'))
        except:
            break

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Servidor esperando conexión...")
    
    palabra = random.choice(lista)
    print(f"Palabra a adivinar: {palabra}")
    while True:
        conn, addr = s.accept()
        
        t = threading.Thread(target=ahorcado, args=(palabra, conn))
        t.start()







