#!/usr/bin/env python
# coding: utf-8

# In[8]:


def pedirnumeros():
    l=[]
    seguir=True
    while seguir:
        try:
            aux=int(input('\nIntroduce algún número, o introduce 0 si deseas finalizar: '))
            if aux!=0:
                l.append(aux)
            else:
                seguir=False
        except:
            print("\nIntroduce un número por favor... \n")
    return l
            


# In[7]:


def maximo(l):
    max=l[0]
    for i in range(len(l)):
        if l[i]>max:
            max=l[i]
    print("\nEl maximo es ", max)


# In[6]:


lista=pedirnumeros()
maximo(lista)


# In[ ]:




