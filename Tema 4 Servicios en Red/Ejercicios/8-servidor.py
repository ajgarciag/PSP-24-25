import socket,threading,random


HOST = '127.0.0.1'
PORT = 2000
numero_secreto = 0
clientes = []
lock = threading.Lock()

def manejar_cliente(conn, addr):
    global numero_secreto
    print(f"[NUEVO JUGADOR] {addr} se ha conectado.")
    conn.send("Bienvenido al juego! Adivina el número entre 1 y 100".encode('utf-8'))
    
    while True:
        try:
            intento = conn.recv(1024).decode('utf-8')
            intento = int(intento)
            
            with lock:
                if intento == numero_secreto:
                    mensaje_ganador = f"Has adivinado el número {numero_secreto}! Reiniciando juego..."
                    conn.send(mensaje_ganador.encode('utf-8'))
                    mensaje= f"Ej jugador {addr} ha adivinado el número {numero_secreto}! Reiniciando juego..."
                    print(mensaje)
                    avisar(mensaje,conn)
                    break
                elif intento < numero_secreto:
                    conn.send("Más alto".encode('utf-8'))
                else:
                    conn.send("Más bajo".encode('utf-8'))
        except:
            break
    
    print(f"[DESCONECTADO] {addr} se ha desconectado.")
    clientes.remove(conn)
    conn.close()

def avisar(mensaje,cliente_ganador):
    for cliente in clientes:
        try:
            if cliente != cliente_ganador: #avisar a todos menos al ganador (ya está avisado)
                cliente.send(mensaje.encode('utf-8'))
        except:
            cliente.close()
            clientes.remove(cliente)

def iniciar_servidor():
    global numero_secreto
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((HOST, PORT))
    servidor.listen()
    print(f"[ESCUCHANDO] Servidor iniciado en {HOST}:{PORT}")
    
    while True:
        cliente, direccion = servidor.accept()
        if not clientes: #si no hay ningun cliente conectado aún en la lista de clientes, piensa un nuevo numero 
            numero_secreto = random.randint(1, 100)
            print(f"Numero a adivinar {numero_secreto}")
        clientes.append(cliente)
        hilo = threading.Thread(target=manejar_cliente, args=(cliente, direccion))
        hilo.start()

if __name__ == "__main__":
    iniciar_servidor()
