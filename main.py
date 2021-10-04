# Observacion se usa la notacion de dx/dt que seria equivalente a dy/dx en otras notaciones.

import numpy as np
import matplotlib.pyplot as plt

#euler
def euler(f, t0, tf, x0, n):
    t = np.linspace(t0, tf, n+1)
    x = np.zeros(n+1)
    x[0] = x0
    h = (tf - t0)/n
    for i in range(1, n+1):
        x[i]= x[i-1] + h * f(t[i-1],x[i-1])
    return ((t,x))

#euler mejorado
def eulerMej(f, t0, tf, x0, n):
    t = np.linspace(t0, tf, n+1)
    x = np.zeros(n+1)
    predictor = np.zeros(n+1)
    predictor[0] = None
    x[0] = x0
    h = (tf - t0)/n
    for i in range(1, n+1):
        predictor[i]= x[i-1] + h * f(t[i-1],x[i-1])
        x[i]= x[i-1] + (h/2) * (f(t[i-1],x[i-1]) + f(t[i],predictor[i]))
    return ((t,x))


 # ejemplo de una funcion problema   
def f(t,x):
     #y = (50*t**2-10*x)/3
     #y = eval('a(50*t**2-10*x)/3')
     #y = 0.5*(-x+t**2+4*t-1)
     y = -2*x  #0, 1, 1, 50
     #y = x-t
     return (y)
#200 iteraciones
(t,x) = euler(f, 0, 1, 1, 100)
(u,y) = eulerMej(f, 0, 1, 1, 50)
plt.plot(t,x,label = 'euler')
plt.plot(u,y,label='euler mejorado')
plt.scatter(t,x)
plt.scatter(u,y)
plt.legend(loc= 'upper left')
plt.show()
