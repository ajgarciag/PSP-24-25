import socket, threading,random, time

HOST = '127.0.0.1'  
PORT = 2000

clientes_clima = []
clientes_deportes = []
clientes_noticias = []
notificaciones =[["Hoy hace sol", "hoy está lloviendo","hace viento"],["Ha ganado Rafa Nadal","Ha perdido el Betis"],["Alto al fuego en Gaza","La deuda pública sigue subiendo"]]

def enviar_notificaciones():
    global notificaciones,clientes_clima, clientes_deportes, clientes_noticias
    while True:
        time.sleep(3)
        tema = random.randint(0,2)
        if tema == 0:
            mensaje = random.choice(notificaciones[0])
            for cliente in clientes_clima:
                cliente.send(mensaje.encode('utf-8'))
        if tema == 1:
            mensaje = random.choice(notificaciones[1])
            for cliente in clientes_deportes:
                cliente.send(mensaje.encode('utf-8'))
        if tema == 2:
            mensaje = random.choice(notificaciones[2])
            for cliente in clientes_noticias:
                cliente.send(mensaje.encode('utf-8'))


def manejar_cliente(cliente):
    while True:
        try:
            mensaje = cliente.recv(1024).decode('utf-8')
            if mensaje == '1':
                if cliente not in clientes_clima:
                    clientes_clima.append(cliente)
            elif mensaje == '2':
                if cliente not in clientes_deportes:
                    clientes_deportes.append(cliente)
            elif mensaje == '3':
                if cliente not in clientes_noticias:
                    clientes_noticias.append(cliente)
            elif mensaje =='desconectar':
                print(f"[DESCONECTADO] Cliente desconectado")
                if cliente in clientes_clima:
                    clientes_clima.remove(cliente)
                if cliente in clientes_deportes:
                    clientes_deportes.remove(cliente)  # Elimina el cliente de la lista
                if cliente in clientes_noticias:
                    clientes_noticias.remove(cliente) 
                cliente.close()
        except:
            print(f"[DESCONECTADO] Cliente desconectado")
            if cliente in clientes_clima:
                clientes_clima.remove(cliente)
            if cliente in clientes_deportes:
                clientes_deportes.remove(cliente)  # Elimina el cliente de la lista
            if cliente in clientes_noticias:
                clientes_noticias.remove(cliente) 
            cliente.close()
            break



def iniciar_servidor():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((HOST, PORT))
    servidor.listen()
    print(f"[ESCUCHANDO] Servidor iniciado en {HOST}:{PORT}")
    #este método enviará de forma aleatoria notificaciones a los clientes que haya conectados
    hilo_notif = threading.Thread(target=enviar_notificaciones) 
    hilo_notif.start()
    while True:
        cliente, direccion = servidor.accept()
        print(f"Se conectó un cliente en la dirección {direccion}")
        hilo = threading.Thread(target=manejar_cliente, args=(cliente,))
        hilo.start()

if __name__ == "__main__":
    iniciar_servidor()
