import socket, random

HOST = '127.0.0.1'  # loopback
PORT = 2000        # Puerto de escucha


with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT)) #emparejo el socket con la direccion Host+Puerto

    n = random.randint(1,100)
    print("He elegido un número del 1 al 100, intenta adivinarlo")
    while True:
        intento, adrr = s.recvfrom(1024)

        if int(intento.decode('utf-8'))== n:
            s.sendto(b"Correcto!",adrr)
            break
        elif int(intento.decode('utf-8')) > n:
            s.sendto(b"Menor",adrr)
        else:
            s.sendto(b"Mayor",adrr)

    print(f"El cliente ha acertado, el número era {n}")
