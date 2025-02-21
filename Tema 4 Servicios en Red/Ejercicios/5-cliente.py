import socket, threading

HOST = '127.0.0.1'  
PORT = 2000



def recibir_mensajes(cliente):
    while True:
        try:
            mensaje = cliente.recv(1024).decode('utf-8')
            print(f"Mensaje recibido:{mensaje}")
        except Exception as e:
            print(f"Error: {e}")
            cliente.close()
            break

def iniciar_cliente():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((HOST,PORT))

    print("Conectado al chat. Escribe un mensaje y presiona enter.")
    t = threading.Thread(target=recibir_mensajes, args=(cliente,))
    t.start()

    while True:
        mensaje = input()
        if mensaje == "salir":
            cliente.close()
            break
        else:
            cliente.send(mensaje.encode('utf-8'))
    
if __name__ == "__main__":
    iniciar_cliente()