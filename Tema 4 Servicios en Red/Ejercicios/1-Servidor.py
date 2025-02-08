'''
import socket
HOST = '127.0.0.1'  
PORT = 2000 
#_ _ _ _ _ 
def esPalindromo(cadena):
    cadena = cadena.lower()
    cadena2 = cadena[::-1]
    return cadena.replace(" ","") == cadena2.replace(" ","")

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print(f"Socket servidor UDP establecido en la direccion {HOST}:{PORT}")
    while True:
        cadena, adrr = s.recvfrom(1024)
        if cadena == b"exit":
            s.sendto(b"Cerrando el servidor...", adrr)
            print("Cerrando el servidor...")
            break
        else:
            resultado = esPalindromo(cadena.decode('utf-8'))
            if resultado:
                s.sendto(b"La cadena mandanda es un palindromo", adrr)
            else:
                s.sendto(b"La cadena mandanda no es un palindromo", adrr)

'''


import socketserver

class PalindromoHandler(socketserver.BaseRequestHandler):
    def es_palindromo(self, cadena):
        cadena = cadena.lower().replace(" ", "")
        return cadena == cadena[::-1]

    def handle(self):
        print(f"cliente conectado: {self.client_address}")
        data = self.request[0].strip()
        socket = self.request[1] #socket servidor
        mensaje = data.decode('utf-8')
        
        if mensaje.lower() == "exit":
            socket.sendto(b"Cerrando conexion...", self.client_address)
            print("Cerrando conexion...")
            return
        
        resultado = self.es_palindromo(mensaje) #true o false
        if resultado:
            respuesta = ("La cadena enviada es un palindromo").encode('utf-8')
        else:
            respuesta = ("La cadena enviada no es un palindromo").encode('utf-8')
        
        socket.sendto(respuesta, self.client_address)

if __name__ == "__main__":
    HOST, PORT = "127.0.0.1", 2000
    with socketserver.UDPServer((HOST, PORT), PalindromoHandler) as server:
        print(f"Socket servidor UDP establecido en la dirección {HOST}:{PORT}")
        server.serve_forever()