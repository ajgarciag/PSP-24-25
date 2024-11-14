#!/usr/bin/env python
# coding: utf-8

import threading,time

def secuencia(n1,n2):
    #time.sleep(5)
    if n1<n2:
        print("La secuencia entre los números es: ", end="")
        for i in range(n1,n2+1):
            print(f"{i}, ", end="")
    else: 
        print(f"No se cumple que {n1}<{n2}")
n1,n2 = 3,60
t = threading.Thread(target=secuencia, args=(n1,n2))
#t.daemon = True
t.start()
print(f"\nLa diferencia de los números es {n2-n1}")





