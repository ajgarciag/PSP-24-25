#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def esPalindromo():
    cadena = input("Introduce una cadena para ver si es palíndromo o no: ")
    if len(cadena)==0:
        print("La cadena está vacía")
        return 0
    else:
        cadena = cadena.lower()
        aux = ''.join(c for c in cadena if c!=' ')
        if aux[::-1]==aux:
            print("La cadena es un palíndromo")
        else:
            print("La cadena no es un palíndromo")


# In[ ]:


esPalindromo()

