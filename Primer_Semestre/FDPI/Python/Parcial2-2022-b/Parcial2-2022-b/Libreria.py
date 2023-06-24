from tkinter import *

def calcular():
    print("Completar")

def totales():
    print("Completar")
 
gui=Tk()
gui.geometry("370x210")

marco1=Frame(gui)
LLibros=Label(marco1,text="Libros")
LRevistas=Label(marco1,text="Revistas")
ELibros=Entry(marco1,width=10)
ERevistas=Entry(marco1,width=10)
LLibros.grid(row=0,column=0)
ELibros.grid(row=0,column=1)
LRevistas.grid(row=1,column=0)
ERevistas.grid(row=1,column=1)

marco2=Frame(gui)
LVenta=Label(marco2,text="Valor a pagar en la venta actual")
EVenta=Entry(marco2,width=15)
LVenta.grid(row=0,column=0)
EVenta.grid(row=0,column=1)

marco3=Frame(gui)
LTotalLibros=Label(marco3,text="Total libros vendidos")
ETotalLibros=Entry(marco3,width=15)
LTotalRevistas=Label(marco3,text="Total revistas vendidas")
ETotalRevistas=Entry(marco3,width=15)
LTotalLibros.grid(row=0,column=0)
ETotalLibros.grid(row=0,column=1)
LTotalRevistas.grid(row=1,column=0)
ETotalRevistas.grid(row=1,column=1)
BCalcular=Button(gui,text="Calcular valor venta",command=calcular)
BTotales=Button(gui,text="Calcular totales",command=totales)

marco1.pack()
BCalcular.pack()
marco2.pack()
BTotales.pack()
marco3.pack()

gui.mainloop()
