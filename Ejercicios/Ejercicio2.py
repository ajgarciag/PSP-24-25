#!/usr/bin/env python
# coding: utf-8

# In[15]:


def contar(ruta,letra):
    with open(ruta,'r', encoding='utf-8') as archivo:
        letra=letra.lower()
        contenido = archivo.read() #guardamos el contenido en una variable. Se guarda como 'str'
        contenido2 = contenido.lower() #pasamos todas las letras a minúsculas, para contar bien
        contador = contenido2.count(letra)
        print(f"Contenido del documento: {contenido}")
        #print(f"La letra {letra} aparece {contador} veces.")
        return contador


# In[19]:


import sys


# In[20]:


def main():
    # Verifica si se pasaron dos argumentos (ruta y letra)
    if len(sys.argv) != 3:
        print("Uso: python nombre_del_script.py <ruta_del_archivo> <letra>")
        sys.exit(-1)

    ruta_archivo = sys.argv[1]
    letra = sys.argv[2]

    # Verifica que se haya pasado solo un carácter como letra
    if len(letra) != 1:
        print("Error: debe proporcionar exactamente un carácter como letra.")
        sys.exit(-1)

    # Contar caracteres
    resultado = contar(ruta_archivo, letra)
    print(f"La letra '{letra}' aparece {resultado} veces en el archivo.")
    sys.exit(0)  # Salida 0 si todo transcurre con normalidad
    


# In[ ]:


if __name__ == "__main__":  
    main()
#En Python, cada módulo (es decir, cada archivo .py) tiene un atributo especial llamado __name__.
#Cuando ejecutas un archivo Python directamente, el valor de __name__ se establece como "__main__".
#Si el archivo es importado como un módulo en otro archivo, __name__ toma el valor del nombre del módulo (es decir, el nombre del archivo sin la extensión .py

