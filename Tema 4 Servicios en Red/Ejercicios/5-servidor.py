
import socket, threading

HOST = '127.0.0.1'  
PORT = 2000

clientes = []



def manejar_cliente(conn):
    while True:
        mensaje = conn.recv(1024).decode('utf-8')
        if mensaje == "salir":
            break
        else:
            enviar_mensaje(mensaje,conn)
    print("Cliente desconectado")
    clientes.remove(conn)
    conn.close()

def enviar_mensaje(mensaje,conn):
    for cliente in clientes:
        if cliente != conn:
            cliente.send(mensaje.encode('utf-8'))



def iniciar_servidor():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((HOST, PORT))
    servidor.listen()

    print(f"[Escuchando] Servidor iniciado en {HOST}:{PORT}")
    while True:
       conn, adrr = servidor.accept() #conn es el socket del cliente
       print(f"Se ha conectado un cliente en la direccion {adrr}")
       clientes.append(conn)
       t = threading.Thread(target= manejar_cliente, args=(conn,))
       t.start()

if __name__ == "__main__":
    iniciar_servidor()
