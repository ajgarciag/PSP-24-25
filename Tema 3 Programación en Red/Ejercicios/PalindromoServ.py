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



