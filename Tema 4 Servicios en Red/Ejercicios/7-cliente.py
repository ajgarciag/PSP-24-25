import socket,threading
HOST = '127.0.0.1'  
PORT = 2000


def recibir_mensajes(cliente):
    while True:
        try:
            #enviar tipo
            mensaje = cliente.recv(1024).decode('utf-8')
            print(f"Notificacion recibida: {mensaje}")
        except Exception as e:
            print(f"Error: {e}")
            cliente.close()
            break




def iniciar_cliente():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((HOST,PORT)) #conexion

    print("Conectado al chat. Escribe:\n 1- Notificaciones clima \n 2- Notificaciones deportes \n 3- Noticias .")
    hilo_recibir = threading.Thread(target=recibir_mensajes, args=(cliente,))
    hilo_recibir.start()
     
    while True:
        mensaje = input()
        if mensaje == "desconectar":
            cliente.send(mensaje.encode('utf-8'))
            cliente.close()
            break
        cliente.send(mensaje.encode('utf-8'))


if __name__ == "__main__":
    iniciar_cliente()


    

    

