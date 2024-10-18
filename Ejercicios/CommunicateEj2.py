#!/usr/bin/env python
# coding: utf-8

# In[14]:


import subprocess

# Iniciar el proceso
#ruta = r"C:\Users\Administrador\Desktop\prueba.txt"
ruta=input("Introduce la ruta al archivo: ")
vocales='aeiou'
for letra in vocales:
    process = subprocess.Popen(["python","Ejercicio2.py",ruta,letra], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Enviar los números al proceso
    output, error = process.communicate()

    print(output.decode('latin1'))
    print(error.decode())
    # Mostrar el resultado
    #print(output.decode())


# In[ ]:




