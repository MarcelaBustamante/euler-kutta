# Observacion se usa la notacion de dx/dt que seria equivalente a dy/dx en otras notaciones.

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
window.title("Graficadora euler y euler mejorado")
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
equ.set('-2*x')
tcero = tk.DoubleVar()
tene = tk.DoubleVar()
tene.set(1)
xcero = tk.DoubleVar()
xcero.set(1)
hon = tk.DoubleVar()
hon.set(100)




canvas.place(x = 0, y = 0)
canvas.create_rectangle(0.0,0.0,252.0,511.0,fill="#3775F5",outline="")

canvas.create_text(8.0,8.0,anchor="nw",text="Tips para uso",fill="#FFFFFF",font=("RedHatDisplay Bold", 20 * -1))
canvas.create_text(8.0,45.0,anchor="nw",text="op sin, cos y raiz usar",fill="#FFFFFF",font=("Roboto", 12 * -1))
canvas.create_text(8.0,59.0,anchor="nw",text="np.sin(x), np.sqrt(x)",fill="#FFFFFF",font=("Roboto", 12 * -1))
canvas.create_text(8.0,73.0,anchor="nw",text="Ejemplo: ",fill="#FFFFFF",font=("Roboto", 12 * -1))
canvas.create_text(8.0,87.0,anchor="nw",text="0.1*np.sqrt(x)+0.4t**2",fill="#FFFFFF",font=("Roboto", 12 * -1))
canvas.create_text(16.0,194.0,anchor="nw",text="Para potencia utilice doble **",fill="#FFFFFF",font=("Roboto", 10 * -1))
canvas.create_text(17.0,362.0,anchor="nw",text="Seleccione N o H",fill="#FFFFFF",font=("Roboto", 10 * -1))
canvas.create_text(8.0,112.0,anchor="nw",text="Ingrese los valores",fill="#FFFFFF",font=("RedHatDisplay Bold", 14 * -1))

#campo 1
entry_image_1 = tk.PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(126.0,169.0,image=entry_image_1)
entry_1 = tk.Entry(bd=0,bg="#FFFFFF",fg="#109DFA",highlightcolor="#109DFA",highlightthickness=0,textvariable=equ)
entry_1.place(x=28.0,y=149.0+19,width=196.0,height=15.0)
canvas.create_text(25.0,151.0,anchor="nw",text="Funcion f(t,x)", fill="#5C5050",font=("RedHatDisplay Medium", 12 * -1))

#Campo 2
entry_image_2 = tk.PhotoImage(file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(126.0,236.0,image=entry_image_2)
entry_2 = tk.Entry(bd=0,bg="#FFFFFF",fg="#109DFA",highlightthickness=0,textvariable=xcero)
entry_2.place(x=28.0,y=216.0+19,width=196.0,height=15.0)
canvas.create_text(25.0,221.0,anchor="nw",text="X(0)",fill="#5C5050",font=("RedHatDisplay Medium", 12 * -1))

#Campo 3
entry_image_3 = tk.PhotoImage(file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(126.0,284.0,image=entry_image_3)
entry_3 = tk.Entry(bd=0,bg="#FFFFFF",fg="#109DFA", highlightthickness=0,textvariable=tcero)
entry_3.place(x=28.0,y=264.0+19,width=196.0,height=15.0)
canvas.create_text(25.0,269.0,anchor="nw",text="T(0)",fill="#5C5050",font=("RedHatDisplay Medium", 12 * -1))

#Campo 4
entry_image_4 = tk.PhotoImage(file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(126.0,332.0,image=entry_image_4)
entry_4 = tk.Entry(bd=0,bg="#FFFFFF",fg="#109DFA", highlightthickness=0,textvariable=tene)
entry_4.place(x=28.0,y=312.0+19,width=196.0,height=15.0)
canvas.create_text(24.0,317.0,anchor="nw",text="T(f)",fill="#5C5050",font=("RedHatDisplay Medium", 12 * -1))

#Radio button
opcion = tk.IntVar()

radio1 = tk.Radiobutton(window,text="H",foreground="#FFFFFF",selectcolor="#123379",activebackground="#3775F5",variable=opcion, value=1,background="#3775F5")
radio1.place(x=120,y=356)

radio2 = tk.Radiobutton(window,text="N",foreground="#FFFFFF",selectcolor="#123379",activebackground="#3775F5",variable=opcion, value=2,background="#3775F5")
radio2.place(x=160,y=356)
radio2.select()

#Campo 5
entry_image_5 = tk.PhotoImage(file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(127.0,404.0,image=entry_image_5)
entry_5 = tk.Entry(bd=0,bg="#FFFFFF",fg="#109DFA",highlightthickness=0,textvariable=hon)
entry_5.place(x=29.0,y=384.0+19,width=196.0,height=15.0)
canvas.create_text(25.0,389.0,anchor="nw",text="Valor N o H",fill="#5C5050",font=("RedHatDisplay Medium", 12 * -1))

#Boton
button_image_1 = tk.PhotoImage(file=relative_to_assets("button_1.png"))
#button_1 = tk.Button(image=button_image_1,borderwidth=0,highlightthickness=0,command=lambda: imprimirVariable(equ,tcero,tene,xcero,hon,opcion),relief="flat")
button_1 = tk.Button(image=button_image_1,borderwidth=0,highlightthickness=0,command=lambda: plot(tcero.get(),tene.get(),xcero.get(), opcion.get(),hon.get()),relief="flat")
button_1.place(x=38.0,y=444.0,width=170.0,height=36.0)

canvas.create_rectangle(8.0,33.0,52.0,37.0,fill="#FFFFFF",outline="")
canvas.create_rectangle(8.0,132.0,52.0,136.0,fill="#FFFFFF",outline="")
 
 #funcion problema   
def f(t,x):
    print(equ)
    print(equ.get())
    y = eval(equ.get())

    return (y)

def plot(tcero, tene, xcero, opcion,hon):
    #calcular
    (t, x, u,y) = calcular(tcero, tene, xcero, opcion, hon)
    #Creción de grafico
    fig = Figure(figsize=(5,4),dpi=100) #dpi - dots per inch
    grafico = fig.add_subplot(111)
    grafico.plot(t,x, color="blue") #Puntos Euler
    grafico.plot(u,y,color="red") #Puntos Euler mejorada
    fig.legend(['Euler', 'Euler mejorada'],)
    #grafico.plot(x,(2*x)**2)
    grafico.set_ylabel("Eje X")
    grafico.set_xlabel("Eje T")
    
    #crea area de dibujo de tkinter
    canvas = FigureCanvasTkAgg(fig, master=window) 
    canvas.draw()
    canvas.get_tk_widget().place(x=288.0,y=10.0,width=500.0,height=459.0)

    #Barra de herramientas
    toolbar = NavigationToolbar2Tk(canvas, window)
    toolbar.update()
    toolbar.place(x=288.0,y=467,width=500.0,height=40)
    


"""SECCION DE CALCULOS"""
def calcular(tcero,tene,xcero,opcion,hon):
    #paso 0 hallo H
    if opcion == 2:
        h = (tene - tcero)/hon
        n = int(hon)
        print('H:', type(h).__name__)
        print('N:', type(n).__name__)
    else:
        h = hon
        n = int((tene - tcero)/hon)
        print('H:', type(h).__name__)
        print('N:', type(n).__name__)

    #evaluo euler y eulerMej
    (t,x) = euler(f, tcero, tene, xcero, h, n)
    (u,y) = eulerMej(f, tcero, tene, xcero, h, n)
    return (t,x,u,y)

#euler
def euler(f, t0, tf, x0, h, n):
    #paso 1  intervalo de puntos discretos
    t = np.linspace(t0, tf, n+1)
    x = np.zeros(n+1)
    x[0] = x0
    #paso 2 calcular Xn
    for i in range(1, n+1):
        x[i]= x[i-1] + h * f(t[i-1],x[i-1])
    return ((t,x))

#euler mejorado
def eulerMej(f, t0, tf, x0, h, n):
    #paso 1
    t = np.linspace(t0, tf, n+1)
    x = np.zeros(n+1)
    predictor = np.zeros(n+1)
    predictor[0] = None
    x[0] = x0
    h = (tf - t0)/n
    for i in range(1, n+1):
        #paso 2
        predictor[i]= x[i-1] + h * f(t[i-1],x[i-1])
        #paso 3
        x[i]= x[i-1] + (h/2) * (f(t[i-1],x[i-1]) + f(t[i],predictor[i]))
    return ((t,x))

window.resizable(False, False)
window.mainloop()
