import threading, random, time

CAPACIDAD = 10
cinta = []

lock_cinta = threading.Lock()  #candado para controlar acceso a la cinta
productos_disponibles = threading.Semaphore(0)  #productos disponibles para consumir
espacios_disponibles = threading.Semaphore(CAPACIDAD)  #espacios disponibles en la cinta

def productor():
    while True:
        producto = random.randint(1, 100)
        espacios_disponibles.acquire()  #esperar que haya espacio
        
        with lock_cinta:  #bloquear acceso a la cinta
            cinta.append(producto)
            print(f"Productor: Producto {producto} añadido. Cinta: {len(cinta)}/{CAPACIDAD}")
        
        productos_disponibles.release()  #notificar producto disponible
        time.sleep(random.uniform(0.1, 0.9))  #simular tiempo de producción

def consumidor():
    while True:
        productos_disponibles.acquire()  #esperar que haya productos
        with lock_cinta: #bloquear acceso a la cinta
            producto = cinta.pop(0)
            print(f"Consumidor: Producto {producto} retirado. Cinta: {len(cinta)}/{CAPACIDAD}")
        
        espacios_disponibles.release()  #liberar un espacio
        time.sleep(random.uniform(0.1, 1))  #simular tiempo de consumo


hilos = []
for _ in range(2):  
    h = threading.Thread(target=productor)
    hilos.append(h)
    h.start()

for _ in range(2): 
    h = threading.Thread(target=consumidor)
    hilos.append(h)
    h.start()