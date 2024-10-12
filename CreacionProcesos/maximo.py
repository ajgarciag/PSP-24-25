#!/usr/bin/env python
# coding: utf-8

# In[24]:


l=input("Introduce numeros separados por comas: ")
l=l.split(',')
print(l)
l=[int(x) for x in l]
print(l)
max=l[0]
for i in range(len(l)):
    if l[i]>max:
        max=l[i]
print("El maximo es ", max)


# In[ ]:




