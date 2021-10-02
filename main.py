# Observacion se usa la notacion de dx/dt que seria equivalente a dy/dx en otras notaciones.

import numpy as np
import matplotlib.pyplot as plt

#euler
def euler(f, t0, tn, x0, n):
    t = np.linspace(t0, tn, n+1)
    x = np.zeros(n+1)
    x[0] = x0
    h = (tn - t0)/n
    for i in range(1, n+1):
        x[i]= x[i-1] + h * f(t[i-1],x[i-1])
    return ((t,x))

#euler mejorado
def eulerMej(f, t0, tn, x0, n):
    t = np.linspace(t0, tn, n+1)
    x = np.zeros(n+1)
    predictor = np.zeros(n+1)
    predictor[0] = x0
    h = (tn - t0)/n
    for i in range(1, n+1):
        predictor[i]= x[i-1] + h * f(t[i-1],x[i-1])
        x[i]= x[i-1] + (h/2) * (f(t[i-1],x[i-1]) + f(t[i-1] + h,predictor[i-1]))
    return ((t,x))
#Runge-Kutta
def RK(f, t0, tn, x0, n):
    t = np.linspace(t0, tn, n+1)
    x = np.zeros(n+1)
    x[0] = x0
    h = (tn-t0)/n
    for i in range(1,n+1):
        k1 = f(t[i-1],x[i-1])
        k2 = f(t[i-1] + h/2, x[i-1] + h*k1/2)
        k3 = f(t[i-1] + h/2, x[i-1] + h*k2/2)
        k4 = f(t[i-1] + h, x[i-1] + h*k3)
        x[i] = x[i-1] + (1/6) * h * (k1 + 2*k2 + 2*k3 + k4)
        return((t,x))

 # ejemplo de una funcion problema   
def f(t,x):
     y = (50*t**2-10*x)/3
     #y = eval('a(50*t**2-10*x)/3')
     return (y)
#200 iteraciones
(t,x) = euler(f, 0, 5, 0, 50)
(u,y) = eulerMej(f, 0, 5, 0, 50)
(v,z) = RK(f, 0, 5, 0, 50)

plt.plot(t,x,label = 'euler')
plt.plot(u,y,label='euler mejorado')
plt.plot(v,z,label='Ruge-Kutta')
plt.legend(loc= 'upper left')
plt.show()
