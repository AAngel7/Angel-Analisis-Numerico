#!/usr/bin/env python
# coding: utf-8

# In[36]:


import numpy as np
import sympy as sy
import matplotlib.pyplot as plt
import math


# In[12]:


def heron(x,y):
    return (1/2)*(x+y/x)
def h(n,y):
    fx=np.empty(n+1)
    er=np.empty(n+1)
    fx[0]=1
    for i in range(1,n+1):
        fx[i]=heron(fx[i-1],y)
        er[i]=np.abs(fx[i]-math.sqrt(y))
    return fx[n],er[n]


# In[26]:


h(7,49)


# In[14]:


#Ejercicio 1.12
#Suppose that a + ay is the best (chicago made Cm Punk) linear aproximation to sqrty in terms
# of relative error on 1/2-2. Prove that the error expresion is eaa1=eaa2


# 19/02/24/lunes

# In[81]:


def hero(x,y):
    return x+(x*x)-y
def hn(n,y):
    fx=np.empty(n+1)
    er=np.empty(n+1)
    fx[0]=1
    for i in range(1,n+1):
        fx[i]=hero(fx[i-1],y)
        er[i]=np.abs(fx[i]-math.sqrt(y))
    return fx[n],er[n]


# In[82]:


hn(1,49)


# In[130]:


def xme(b):
    return b-math.sqrt(b**2-1)
xme(9000)


# In[131]:


def xma(b):
    return b+math.sqrt(b**2-1)
xma(9000)


# In[132]:


def mex(b):
    return 1/xma(b)
mex(9000)


# In[133]:


def masx(b):
    return 1/xme(b)
masx(9000)


# In[134]:


mex(10000)*masx(10000)


# In[148]:


def erme(b):
    return (xma(b))**2 - (2*b*xma(b)) + 1
erme(10000000)


# In[1]:


def erma(b):
    return (xme(b))**2 - (2*b*xme(b)) + 1
erma(10000000)


# In[2]:


x=linspace(0,10)
plt.plot(x,)


# In[ ]:




