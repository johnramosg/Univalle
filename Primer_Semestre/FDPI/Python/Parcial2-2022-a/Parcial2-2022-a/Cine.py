from tkinter import *

def calcular():
    print("Completar")  
    
gui=Tk()
gui.geometry("270x160")

marco1=Frame(gui)
LUbicacion=Label(marco1,text="Ubicación ")
LTipo=Label(marco1,text="Tipo función ")
LCantidad=Label(marco1,text="Cantidad boletos ")
EUbicacion=Entry(marco1,width=15)
ETipo=Entry(marco1,width=15)
ECantidad=Entry(marco1,width=15)
LUbicacion.grid(row=0,column=0)
EUbicacion.grid(row=0,column=1)
LTipo.grid(row=1,column=0)
ETipo.grid(row=1,column=1)
LCantidad.grid(row=2,column=0)
ECantidad.grid(row=2,column=1)

marco2=Frame(gui)
LVenta=Label(marco2,text="Total a pagar ")
EVenta=Entry(marco2,width=15)
LVenta.grid(row=0,column=0)
EVenta.grid(row=0,column=1)

BCalcular=Button(gui,text="Calcular pago",command=calcular)

marco1.pack()
BCalcular.pack()
marco2.pack()

gui.mainloop()
