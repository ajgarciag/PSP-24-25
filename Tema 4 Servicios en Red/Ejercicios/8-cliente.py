import socket

HOST = '127.0.0.1'
PORT = 2000

def iniciar_cliente():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((HOST, PORT))
     #mensaje de bienvenida
    mensaje_inicial = cliente.recv(1024).decode('utf-8')
    print(mensaje_inicial)
    
    while True:
        intento = input("Ingresa tu número: ")
        if intento.lower() == "salir":
            break
        
        cliente.send(intento.encode('utf-8'))
        respuesta = cliente.recv(1024).decode('utf-8')
        print(respuesta)
        
        if "Reiniciando" in respuesta:
            break
    
    cliente.close()

if __name__ == "__main__":
    iniciar_cliente()
