from tkinter import *

def ingresar():
    print("Completar")
    
def pares():
    print("Completar")

def impares():
    print("Completar")
    
gui=Tk()
gui.geometry("350x230")

LNumero=Label(gui,text="Número a ingresar")
ENumero=Entry(gui,width=15)
BIngresar=Button(gui,text="Ingresar",command=ingresar)

BPares=Button(gui,text="Buscar pares menores al límite",command=pares)
BImpares=Button(gui,text="Buscar impares menores al límite",command=impares)

marco1=Frame(gui)
LLimite=Label(marco1,text="Límite")
ELimite=Entry(marco1,width=5)
LLimite.grid(row=0,column=0)
ELimite.grid(row=0,column=1)

marco2=Frame(gui)
LResultado=Label(marco2,text="Números encontrados")
EResultado=Entry(marco2,width=15)
LCantidad=Label(marco2,text="Cantidad")
ECantidad=Entry(marco2,width=15)
LResultado.grid(row=0,column=0)
EResultado.grid(row=0,column=1)
LCantidad.grid(row=1,column=0)
ECantidad.grid(row=1,column=1)

LNumero.pack()
ENumero.pack()
BIngresar.pack()
marco1.pack()
BPares.pack()
BImpares.pack()
marco2.pack()

gui.mainloop()
