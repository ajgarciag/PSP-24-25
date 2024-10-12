#!/usr/bin/env python
# coding: utf-8

# In[5]:


import subprocess

# Solicitar al usuario que ingrese el término de búsqueda
termino_busqueda = input("Introduce el término que deseas buscar: ")

# Formatear la URL de búsqueda de Google
url = f"https://www.google.com/search?q={termino_busqueda}"

# Ejecutar Google Chrome con la URL
subprocess.run(["C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", url])


# In[ ]:




