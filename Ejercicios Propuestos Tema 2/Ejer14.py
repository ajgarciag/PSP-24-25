import threading

def metodo1():
    for i in range (1,101,3):
        with cond:
            cond.wait()
            print(i, end= ' ')
            cond.notify()
def metodo2():
    for i in range (2,100,3):
        with cond:
            cond.wait()
            print(i, end= ' ')
            cond.notify()
def metodo3():
    for i in range (3,100,3):
        with cond:
            cond.wait()
            print(i, end= ' ')
            cond.notify()

cond = threading.Condition()

metodos = [metodo1, metodo2, metodo3]

for metodo in metodos:
    t = threading.Thread(target=metodo)
    t.start()

with cond:
    cond.notify() #despierta al primer hilo que entra en estado 'wait'