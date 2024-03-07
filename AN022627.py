#!/usr/bin/env python
# coding: utf-8

# 26/02/24/lunes

# In[4]:


import numpy as np
import sympy as sy
from sympy import *
from sympy.abc import x
import matplotlib.pyplot as plt


# In[5]:


A=np.array([[1,2,1],[1,2,1],[1,2,1]])
print(A)
F = np.array([3,4,5])
print(F)
G = np.array([2,7,2])
print(G)
U = np.array([[1,2,3],[0,0,0],[0,0,0]])
def al(k,A,F):
    for i in range(k):
        for j in range(0,2):
            U[i,j] = A[i,j] - ((A[i,k])/(A[k,k]))*A[k,j]
    G[k]=F[k] - ((A[i,k])/(A[k,k]))*F[k]
    k+=1
    if k==2:
        x = G[k]/U[k,k]
        return x
    else:
        return al(k,U,G,U,G)


# 27/02/24/martes

# In[6]:


#Substitución pa'tras y pa'lante
#producto escalar np.dot
#matriz L vector x LX=G
g=np.copy(G)
l=np.copy(A)
def fsub(L,G):
    n=3
    x=np.zeros(n)
    xl=np.zeros(n)
    print(x)
    print(xl)
    print(l)
    print(g)
    for i in range(n+1):
        for j in range(i-1):
            xl[j]=l[i,j]*x[j]
            x[i]=(g[i]/l[i,i])-(xl[i]/l[i,i])
        print(x[i])


# In[7]:


fsub(1,2)


# In[ ]:




