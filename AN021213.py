#!/usr/bin/env python
# coding: utf-8

# 12/02/24/lunes
# BIg G notion
# $$f(x)=G(g(x))$$ segun $$x\rightarrow a$$
# $$Si |f(x)|\leq M|g(x)| $$para $$|x-a|<\delta, M,a>0$$
# Ejercicio/ejemplo
# sin(x) alrededor de $$x_0=0$$
# $$sin(x)=\lim{N\to100}(T_{N}(x))$$
# $$T_{N}=\sum_{n=0}^{N}(-1)^{n}\cdot \frac{x^{2n+1}}{(2n+1)1}$$

# In[15]:


import numpy as np
import sympy as sy
import matplotlib.pyplot as plt


# In[16]:


x=sy.symbols('x')
f=sy.exp(x)-3*sy.cos(x)
g=sy.series(f,x,0,5)
print(f)
print(g)


# In[17]:


orden=g.getO()
gx=g.removeO()
print(orden)
print(gx)
ffunc=sy.lambdify(x,f)
gfunc=sy.lambdify(x,g.removeO())
print(ffunc)
print(gfunc)
ffunc(5)


# In[18]:


x=np.linspace(0,5)
yf=ffunc(x)
yg=gfunc(x)
plt.plot(x,yf,color='r')
plt.plot(x,yg,color='b')
yer=np.abs(yf-yg)
yord=x**3
plt.plot(x,yer,color='y')
plt.plot(x,yord,color='g')
plt.legend(['yf','yg','error','orden'])
plt.show()


# 13/02/24/martes
# Error de convergencia
# $$y_0=1 \\ y_1=\frac{1}{5} + \epsilon \\ y_{n+1}=\frac{16}{5}y_n - \frac{3}{5}y_{n-1} $$
# Solución $$ y_n=(\frac{1}{5})^n$$

# In[19]:


n=77
y=np.empty(n+1)
y[0]=1
y[1]=1/5
for i in range(2,n+1):
    y[i]=(16/5)*y[i-1] - (3/5)*y[i-2]
x=np.arange(n+1)
plt.semilogy(x,y,'rx')
plt.semilogy(x,(1/5)**x,'bp')
plt.grid(True)
plt.show()


# In[ ]:




