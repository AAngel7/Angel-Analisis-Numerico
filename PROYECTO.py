#!/usr/bin/env python
# coding: utf-8

# $$\textbf{Pozo de potencial finito}$$
# Considerando una particula de masa m moviendose en el siguiente sistema potencial:
# $$V(x) = \left\{ \begin{array}{lr} V_0 & : x < \frac{-a}{2}\\ 0 & : \frac{-a}{2}\leq x \leq \frac{a}{2}\\ V_0 & : x>\frac{a}{2} \end{array} \right.$$
# ![image-3.png](attachment:image-3.png)
# $$\textbf{Soluciones de dispersión $E>V_0$}$$
# Si la particula inicialmente incide desde la izquierda con un momento constante de valor $\sqrt{2m(E-V_0)}$,
# se acelerará hasta un valor $\sqrt{2mE}$ entre $\frac{-a}{2}\leq x \leq \frac{a}{2}$, luego se ralentizará hasta su momento inicial en la región $x>a$; todas las particulas que vienen desde la izquierda serán transmitidas, ninguna será reflejada, por lo que T=0 y R=1.
# $$\textbf{Las soluciones vinculadas al Estado $0< E < V_0$}$$
# Cuando $E<V_0$ la particula se encuentra confinada en la region $\frac{-a}{2}\leq x \leq \frac{a}{2}$, rebotará de ida y vuelta entre $x=\frac{-a}{2}$ y $x=\frac{a}{2}$ con un momento constante $p=\sqrt{2mE}$.En estas tres regiones la ecuación de Schrodinger se puede escribir como
# $$
# ( \frac{d^2}{d x^2} - k_{1}^2 ) \phi_1(x)=0      x < \frac{-a}{2}       (1)\\
# ( \frac{d^2}{d x^2} + k_{2}^2 ) \phi_2(x)=0      \frac{-a}{2} \leq x \leq \frac{a}{2}       (2)\\
# ( \frac{d^2}{d x^2} - k_{1}^2 ) \phi_3(x)=0      x > \frac{a}{2}       (3)\\
# $$
# donde
# $$
# k_1^2 = \frac{2m(V_0 - E)}{h^2}\\
# k_2^2 = \frac{2mE}{h^2}\\
# $$
# Eliminando las soluciónes fisicamente inaceptables,se puede escribir la solución a la ecuación de Schrodinger en las regiones $x<\frac{-a}{2}$ y $x>\frac{a}{2}$ de la siguiente forma
# $$
# \phi_1(x) = Ae^{k_1 x}      x < \frac{-a}{2}                      (4)\\
# \phi_2(x)=De^{-k_1 x}       x > \frac{a}{2}                       (5)\\
# $$
# Las soluciones de (1) y (3) son
# $$\textbf{Antisimétrico (impar)}$$
# $$
# \phi_a(x) = \left\{ \begin{array}{lr} Ae^{k_1 x} & : x < \frac{-a}{2}\\ Csin(k_2 x) & : \frac{-a}{2}\leq x \leq \frac{a}{2}   (6)\\ De^{-k_1 x} & : x>\frac{a}{2} \end{array} \right.
# $$
# $$\textbf{Simétrico (par)}$$
# $$
# \phi_s(x) = \left\{ \begin{array}{lr} Ae^{k_1 x} & : x < \frac{-a}{2}\\ Bcos(k_2 x) & : \frac{-a}{2}\leq x \leq \frac{a}{2}   (7)\\ De^{-k_1 x} & : x>\frac{a}{2} \end{array} \right.
# $$
# Para determinar los eigenvalores se necesitan condiciones de continuidad $x=\pm\frac{a}{2}$, entonces
# $$
# k_2 cot(\frac{ak_2}{2}) = -k_1                                    (8)\\
# k_2 tan(\frac{ak_2}{2}) = k_1                                     (9)\\
# $$
# Las ecuaciones (8) y (9) no se pueden resolver directamente, por lo que se resolveran grafica o numericamente. Para resolver graficamente, necesitamos escribirlas de la siguiente forma
# $$
# -\alpha_n cot(a_n) = \sqrt{R^2 - a_{n}^2}                         (10)\\
# \alpha_n tan(a_n) = \sqrt{R^2 - a_{n}^2}                          (11)\\
# $$
# Donde $a_{n}^2=\frac{ak_2}{2}^2=\frac{m a^2 E_n}{2h^2}$ y $R^2=\frac{m a^2 V_0}{2h^2}$. El termino de la izquierda de las ecuaciones (10) y (11) consiste en funciones trigonometricas, mientras que el lado derecho consiste en un circulo de radio R. Las soluciones estan dadas en los puntos donde el circulo $\sqrt{R^2 - a_{n}^2}$ intersecta con las funciones $-a_n cot(a_n)$ y $a_n tan(a_n)$. 

# $$\textbf{Programa}$$
# Para resolver las ecuaciones (10) y (11) que corresponden a nuestras eucaiones trascendentales, se emplea el método de Newton_Rapson.Por lo que de la expresión (10) se se tomo la función como se muestra a continuación
# $$
# f=\alpha_n cot(a_n) + \sqrt{R^2 - a_{n}^2}
# $$
# Que cooresnponde a resolver una ecuación no lineal de la forma f(x)=0; de forma similar para (11)
# $$
# g=-\alpha_n tan(a_n) + \sqrt{R^2 - a_{n}^2}
# $$
# Remplazando el valor de $\alpha$ para ambas funciones f y g.
# $$
# f=(\sqrt{\frac{m a^2 E}{2h^2}}) \cdot cot(\sqrt{\frac{m a^2 E_n}{2h^2}}) + \sqrt{R^2 - \frac{m a^2 E}{2h^2}}\\
# g=(-\sqrt{\frac{m a^2 E}{2h^2}}) \cdot tan(\sqrt{\frac{m a^2 E_n}{2h^2}}) + \sqrt{R^2 - \frac{m a^2 E}{2h^2}}\\
# $$
# Las raíces a encontrar corresponden a la energpia (E), por lo que f y g son funciones de E,por lo tanto los demás valores podemos considerarlos como constantes al mometo de obtnere la derivada, por lo tanto sea $L=\sqrt{m a^2}{2 h^2}$, f y g se puden escribir como
# $$
# f(E)=L \sqrt{E} cot(L \sqrt) + \sqrt{R^2 - L^2 E}\\
# g(E)=-L \sqrt{E} tan(L \sqrt) + \sqrt{R^2 - L^2 E}
# $$
# Entonces la derivadas de f y g son
# $$
# f'(E)=\frac{Lcot(L\sqrt{E})}{2\sqrt{E}}-\frac{k^2 csc^2(L\sqrt{E})}{2}-\frac{L^2}{2\sqrt{R^2-L^2 E}}\\
# g'(E)=-\frac{Ltan(L\sqrt{E})}{2\sqrt{E}}-\frac{k^2 sec^2(L\sqrt{E})}{2}-\frac{L^2}{2\sqrt{R^2-L^2 E}}\\
# $$
# Ahora con esto pasamoa a definir algunas funciones, que calculan el valor de $\alpha$,R,L,f(E),f'(E),g(E) y g'(E) respectivamente
# $$
# \textit{Función alpha(m,a,e0)}\\
# \alpha = \sqrt{\frac{m a^2 e0}{2 h^2}}\\
# \textit{Función radio(m,a,v0)}\\
# R^2 = \frac{m a^2 v0}{2 h^2}\\
# \textit{Función const(m,a)}\\
# L = \sqrt{\frac{m a^2}{2 h^2}}\\
# \textit{Función f(m,a,v0,e0)}\\
# f = \alpha cot(\alpha) + \sqrt{R^2 - \alpha^2}\\
# \textit{Función fprima(m,a,v0,e0)}\\
# f' = \frac{Lcot(L\sqrt{E})}{2\sqrt{e}}-\frac{k^2 csc(k\sqrt{e})^2}{2}-\frac{k^2}{2\sqrt{R^2-k^2 e}}\\
# \textit{Función g(m,a,v0,e0)}\\
# g = -\alpha_n tan(a_n) + \sqrt{R^2 - a_{n}^2}\\
# \textit{Función gprima(m,a,v0,e0)}\\
# f' = -\frac{Ltan(L\sqrt{E})}{2\sqrt{E}}-\frac{k^2 sec^2(L\sqrt{E})}{2}-\frac{L^2}{2\sqrt{R^2-L^2 E}}\\
# $$

# In[3]:


import numpy as np
import sympy as sy
import matplotlib.pyplot as plt
import math
from mpmath import cot
from mpmath import csc
from mpmath import sec


# In[4]:


#masa m
#profundidad V0
#ancho a
#energía E
#constante reducida de plank h
h=6.63*(10**(-34))
def profundidad(m,a):
    return (((sy.pi)/2)**2)**((2*(h**2))/(m*(a**2)))
def alpha(m,a,e0):
    return ((m*(a**2)*e0)/(2*(h**2)))**(1/2)
def radio(m,a,v0):
    return ((m*(a**2)*v0)/(2*(h**2)))**2
def const(m,a):
    return ((m*(a**2))/(2*(h**2)))**(1/2)
def f(m,a,v0,e0):
    return ((alpha(m,a,e0)*cot(alpha(m,a,e0)))+(radio(m,a,v0)-(alpha(m,a,e0))**2)**(1/2))
def fprima(m,a,v0,e0):
    return ((const(m,a)/(2*(e0**(1/2))))*cot(const(m,a)*(e0**(1/2))) - ((const(m,a)**2)/2)*((csc(const(m,a)*(e0**(1/2))))**2) - ((const(m,a)**2)/(2*((radio(m,a,v0) - ((const(m,a)**2)*e0))**(1/2)))))
def g(m,a,v0,e0):
    return ((-alpha(m,a,e0)*math.tan(alpha(m,a,e0)))+(radio(m,a,v0)-(alpha(m,a,e0))**2)**(1/2))
def gprima(m,a,v0,e0):
    return ((-const(m,a)/(2*(e0**(1/2))))*math.tan(const(m,a)*(e0**(1/2))) + ((const(m,a)**2)/2)*((sec(const(m,a)*(e0**(1/2))))**2) - ((const(m,a)**2)/(2*((radio(m,a,v0) - ((const(m,a)**2)*e0))**(1/2)))))


# In[5]:


#Newton-Rapson
def newton1(m,a,v0,e0,tol=1e-6,max_iter=1000):
    itera=0
    while True:
        fx=f(m,a,v0,e0)
        fxprima=fprima(m,a,v0,e0)
        if abs(fxprima) < 1e-12:
            raise ValueError("Derivada cercana a cero.")
        e1 = e0 - (fx/fxprima)
        if abs(e1 - e0) < tol or itera >= max_iter:
            raiz = e1
            break
        e0 = e1
        itera += 1
    return raiz, itera


# In[6]:


rai, iteraciones = newton1(0.0000000002,0.00000000011,0.0000000002,0.00015)
print("Raíz encontrada:", rai)
print("Iteraciones realizadas:", iteraciones)


# In[7]:


def newton2(m,a,v0,e0,tol=1e-6,max_iter=1000):
    itera=0
    while True:
        gx=g(m,a,v0,e0)
        gxprima=gprima(m,a,v0,e0)
        if abs(gxprima) < 1e-12:
            raise ValueError("Derivada cercana a cero.")
        e1 = e0 - (gx/gxprima)
        if abs(e1 - e0) < tol or itera >= max_iter:
            raiz = e1
            break
        e0 = e1
        itera += 1
    return raiz, itera


# In[8]:


rai, iteraciones = newton2(0.0000000002,0.00000000011,0.0000000002,0.0000000005)
print("Raíz encontrada:", rai)
print("Iteraciones realizadas:", iteraciones)


# El número de soluciones dependerá del tamaño de R, que a su vez depende de la profundidad del pozo $V_0$ y su ancho $a$, entonces $R=\sqrt{\frac{m a^2 V_0}{2h^2}}$. Cuanto más profundo y amplio sea el pozo, mayor será el valor de R, y por lo tanto mayor el número de estados unidos. Tenga en cuenta que siempre hay al menos un estado limitado (es decir, una intersección) no importa lo pequeño que sea $V_0$.Cuando
# $0<R<\frac{\pi}{2}$ o $0<V_0<\frac{\pi}{2}^2 \frac{2 h^2}{m a^2}$
# Solo hay un estado correspondiente a n=0,este estado es par: Entonces cuando se tiene
# $\frac{\pi}{2}<R<\pi$ o $\frac{\pi}{2}^2 \frac{2 h^2}{m a^2}<V_0<\pi^2 \frac{2 h^2}{m a^2}$
# Hay dos estados, uno que corresponde a n=0 (par) y un estdao impar en n=1. Ahora si se tiene
# $\pi<R<\frac{3\pi}{2}$ o $\pi^2 \frac{2 h^2}{m a^2}<V_0<\frac{3\pi}{2}^2 \frac{2 h^2}{m a^2}$
# Hay tres estados correspondientes a n=0,1,3.Entonces de forma general los n estados estan dados como
# $R=\frac{\pi}{2}n$ o $V_0=\frac{\pi}{2}^2 \frac{2 h^2}{m a^2}n^2$
# El espectro consiste entonces en un en un alternado de estados pares e impares. En el limite cunado $V_0\rightarrow \infty$ el circulo de radio R también tiende a infinito, por lo que la función $R=\sqrt{\frac{m a^2 V_0}{2h^2}}$ intersectara a $-\alpha_n cot(\alpha_n)$ y $\alpha_n tan(\alpha_n)$ en las asintotas $\alpha=\frac{\pi}{2}n$, esto es debido a que cuando $V_0\rightarrow \infty$, tanto tan como cot también tienden a infinito, entonces
# $$
# tan(\alpha_n)\rightarrow \infty \Rightarrow \alpha_n=\frac{2n+1}{2}\pi\\
# cot(\alpha_n)\rightarrow \infty \Rightarrow \alpha_n=n\pi\\
# $$
# Combinando estos dos casos obtenemos que 
# $$
# \alpha_n=\frac{\pi}{2}n  (1,2,3,...)
# $$
# Derivado de la definición de $\alpha$ podemos obtener una expresión de la energípa de un pozo de potencial finito
# $$
# \alpha_n = \frac{n\pi}{2} \Rightarrow E_n = \frac{\pi^2 h^2}{2m a^2}n^2
# $$

# In[31]:


from sympy import *
x=sy.symbols('x')
f=x*sy.tan(x)
print(f)
ffunc=sy.lambdify(x,f)
print(ffunc)
x=np.linspace(0,2*math.pi)
yf=ffunc(x)
plt.plot(x,yf,color='r')
plt.legend(['atana','acota'])
plt.grid()
plt.show()


# [1] https://www.fisicacuantica.es/pozo-cuadrado-finito/
# 
# [2] http://hyperphysics.phy-astr.gsu.edu/hbasees/quantum/pfbox.html
# 
# [3] http://www.sc.ehu.es/sbweb/fisica3/cuantica/pozo/pozo.html
# 
# [4] http://www.sc.ehu.es/sbweb/fisica/cuantica/pozo/pozo.htm
