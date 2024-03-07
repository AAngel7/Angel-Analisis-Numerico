#!/usr/bin/env python
# coding: utf-8

# In[6]:


#KEPLER'S EQUATION
#ENCONTRAR RAÍCES NEWTON-RHAPSON.SIMPSON
#NEWTON PROPUSO 
import numpy as np


# In[7]:


def gn(x,t,e):
    return x + (t-x+e*np.sin(x))/(1-e*np.cos(x))
def gk(x,t,e):
    return t+e*sy.sin(x)
def gh(x,y):
    return (1/2)*(x+y/x)
def kgn(e,t):
    p=0.7
    print(p)
    while p != gn(p,t,e):
        p = gn(p,t,e)
        print(p)
    return p
def kgk(e,t):
    p=0.7
    print(p)
    while p != gk(p,t,e):
        p = gk(p,t,e)
        print(p)
    return p
def nrs(g,x0,e,t):
    p=0.7
    p=x0
    print(p)
    while p != g(p,t,e):
        p = g(p,t,e)
        print(p)
    return p


# In[8]:


kgn(0.1,0.1)


# 

# In[ ]:




