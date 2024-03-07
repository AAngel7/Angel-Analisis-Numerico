#!/usr/bin/env python
# coding: utf-8

# 12/02/24/lunes
# Dada una función f(x), determinar el orden de aproximación O si requqrimos que el resto R_n(x) sea menor que cierto valor npumerico dado (tolerancia).
# Se que $$R_n(x)=f(x) - T_n(x)$$
# Cuando tu resto es cero tu función es igual a tu serie de taylor
# 
# 

# In[5]:


import numpy as np
import sympy as sy
import matplotlib.pyplot as plt


# In[7]:


n=1000
x=sy.symbols('x')
f=sy.sin(x) + sy.cos(x)
print("Función f(x):",f)
ffunc=sy.lambdify(x,f)
print(ffunc)


# In[10]:


def tol(t,h):
    for i in range(1,n):
        g=sy.series(f,x,0,i)
        gfunc=sy.lambdify(x,g.removeO())
        ff=ffunc(h)
        gg=gfunc(h)
        r=np.abs(ff-gg)
        if r<t:
            print("Función f(x):",f)
            print("Tolerancia:",t)
            print("Serie de Taylor:",g)
            print("Orden de aproximación:",i)
            break
        else:
            continue


# In[11]:


tol(0.1,7)


# 16/02/24/jueves
# Ejercicio 1.12
# Suppose that a + ay is the best (chicago made Cm Punk) linear aproximation to sqrty in terms
# of relative error on 1/2-2. Prove that the error expresion is eaa1=eaa2

# In[ ]:




