#import matplotlib.figure as plt
from math import exp
import numpy as np
from pathlib import Path
import tkinter as tk

#Agregadas por mi,ver si borro
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
from numpy.lib.function_base import gradient


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

#Creo la ventana de tkinter
window = tk.Tk()
window.geometry("801x511")
window.configure(bg = "#FFFFFF")
canvas = tk.Canvas(
    window,
    bg = "#FFFFFF",
    height = 511,
    width = 801,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

def imprimirVariable(equ, tcero, tene, xcero,hon,opcion):
    print(equ.get())
    print(tcero.get())
    print(tene.get())
    print(xcero.get())
    print(hon.get())
    print(opcion.get())



#Variables
equ = tk.StringVar()
tcero = tk.IntVar()
tene = tk.IntVar()
xcero = tk.DoubleVar()
hon = tk.DoubleVar()



canvas.place(x = 0, y = 0)
canvas.create_rectangle(0.0,0.0,252.0,511.0,fill="#3775F5",outline="")

canvas.create_text(8.0,8.0,anchor="nw",text="Bienvenido",fill="#FFFFFF",font=("RedHatDisplay Bold", 20 * -1))
canvas.create_text(8.0,45.0,anchor="nw",text="Este graficador le pertmitria",fill="#FFFFFF",font=("Roboto", 12 * -1))
canvas.create_text(8.0,59.0,anchor="nw",text="introducir una función y aproximarla",fill="#FFFFFF",font=("Roboto", 12 * -1))
canvas.create_text(8.0,73.0,anchor="nw",text="por los metodos de Euler, ",fill="#FFFFFF",font=("Roboto", 12 * -1))
canvas.create_text(8.0,87.0,anchor="nw",text="Euler Mejorada y Runge kutta",fill="#FFFFFF",font=("Roboto", 12 * -1))
canvas.create_text(16.0,194.0,anchor="nw",text="Para potencia utilice doble **",fill="#FFFFFF",font=("Roboto", 10 * -1))
canvas.create_text(17.0,362.0,anchor="nw",text="Seleccione N o H",fill="#FFFFFF",font=("Roboto", 10 * -1))
canvas.create_text(8.0,112.0,anchor="nw",text="Ingrese los valores",fill="#FFFFFF",font=("RedHatDisplay Bold", 14 * -1))

#campo 1
entry_image_1 = tk.PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(126.0,169.0,image=entry_image_1)
entry_1 = tk.Entry(bd=0,bg="#FFFFFF",highlightthickness=0,textvariable=equ)
entry_1.place(x=28.0,y=149.0+19,width=196.0,height=15.0)
canvas.create_text(25.0,151.0,anchor="nw",text="Funcion f(x,t)", fill="#5C5050",font=("RedHatDisplay Medium", 12 * -1))

#Campo 2
entry_image_2 = tk.PhotoImage(file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(126.0,236.0,image=entry_image_2)
entry_2 = tk.Entry(bd=0,bg="#FFFFFF",highlightthickness=0,textvariable=xcero)
entry_2.place(x=28.0,y=216.0+19,width=196.0,height=15.0)
canvas.create_text(25.0,221.0,anchor="nw",text="X(0)",fill="#5C5050",font=("RedHatDisplay Medium", 12 * -1))

#Campo 3
entry_image_3 = tk.PhotoImage(file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(126.0,284.0,image=entry_image_3)
entry_3 = tk.Entry(bd=0,bg="#FFFFFF",highlightthickness=0,textvariable=tcero)
entry_3.place(x=28.0,y=264.0+19,width=196.0,height=15.0)
canvas.create_text(25.0,269.0,anchor="nw",text="T(0)",fill="#5C5050",font=("RedHatDisplay Medium", 12 * -1))

#Campo 4
entry_image_4 = tk.PhotoImage(file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(126.0,332.0,image=entry_image_4)
entry_4 = tk.Entry(bd=0,bg="#FFFFFF",highlightthickness=0,textvariable=tene)
entry_4.place(x=28.0,y=312.0+19,width=196.0,height=15.0)
canvas.create_text(24.0,317.0,anchor="nw",text="T(f)",fill="#5C5050",font=("RedHatDisplay Medium", 12 * -1))

#Radio button
opcion = tk.IntVar()
radio1 = tk.Radiobutton(window,text="H",foreground="#FFFFFF",selectcolor="#123379",activebackground="#3775F5",variable=opcion, value=1,background="#3775F5")
radio1.place(x=120,y=356)

radio2 = tk.Radiobutton(window,text="N",foreground="#FFFFFF",selectcolor="#123379",activebackground="#3775F5",variable=opcion, value=2,background="#3775F5")
radio2.place(x=160,y=356)

#Campo 5
entry_image_5 = tk.PhotoImage(file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(127.0,404.0,image=entry_image_5)
entry_5 = tk.Entry(bd=0,bg="#FFFFFF",highlightthickness=0,textvariable=hon)
entry_5.place(x=29.0,y=384.0+19,width=196.0,height=15.0)
canvas.create_text(25.0,389.0,anchor="nw",text="Valor N o H",fill="#5C5050",font=("RedHatDisplay Medium", 12 * -1))

#Boton
button_image_1 = tk.PhotoImage(file=relative_to_assets("button_1.png"))
#button_1 = tk.Button(image=button_image_1,borderwidth=0,highlightthickness=0,command=lambda: imprimirVariable(equ,tcero,tene,xcero,hon,opcion),relief="flat")
button_1 = tk.Button(image=button_image_1,borderwidth=0,highlightthickness=0,command=lambda: plot(t,x,u,y),relief="flat")
button_1.place(x=38.0,y=444.0,width=170.0,height=36.0)

canvas.create_rectangle(8.0,33.0,52.0,37.0,fill="#FFFFFF",outline="")
canvas.create_rectangle(8.0,132.0,52.0,136.0,fill="#FFFFFF",outline="")

def plot(t,x,u,y):
    #Creción de grafico
    fig = Figure(figsize=(5,4),dpi=100) #dpi - dots per inch

    #rango numerico del grafico
    #x = np.arange(tcero,tene,.01)
    #funcion a graficar

    grafico = fig.add_subplot(111)
    #x=[0,0.2,0.4,0.6,0.8,1]
    #y=[1,0.6,0.36,0.22,0.13,0.08]
    #q=[1,2,3,4,5]
    #z=[1,2,3,4,5]
    grafico.plot(t,x) #Puntos Euler
    grafico.plot(u,y) #Puntos Euler mejorada
    #grafico.plot(x,(2*x)**2)
    grafico.set_ylabel("Eje X")
    grafico.set_xlabel("Eje T")
    
    #crea area de dibujo de tkinter
    canvas = FigureCanvasTkAgg(fig, master=window,) 
    canvas.get_tk_widget().place(x=280.0,y=20.0,width=503.0,height=459.0)
    canvas.draw()

    """ Estas lineas agregan la barra de herramientas
       toolbar = NavigationToolbar2Tk(grafico,window)
        toolbar.update()
        grafico.get_tk_widget().place(x=280.0,y=20.0,width=503.0,height=459.0)
    """

"""SECCION DE CALCULOS JULY"""

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
     y = 0.5*(-x+t**2+4*t-1)
     #y = -2*x  #0, 1, 1, 50
     #y = x-t
     return (y)
#200 iteraciones
(t,x) = euler(f, 0, 1, 1, 100)
(u,y) = eulerMej(f, 0, 1, 1, 50)


window.resizable(False, False)
window.mainloop()
