#!/usr/bin/env python
# coding: utf-8

# In[10]:


import threading

def secuencia(n1,n2):
    if n1<n2:
        for i in range(n1,n2+1):
            if i!=n2:
                print(i,end=",")
            else: 
                print(i)
    else: 
        print(f"No se cumple que {n1}<{n2}")
n1,n2 = 10,10000
t = threading.Thread(target=secuencia, args=(n1,n2))
t.daemon = True
t.start()
print(f"La diferencia entre los números es {n2-n1}")

