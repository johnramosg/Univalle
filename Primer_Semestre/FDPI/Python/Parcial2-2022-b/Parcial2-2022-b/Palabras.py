from tkinter import *

def ingresar():
    print("Completar")
    
def calcular():
    print("Completar")

gui=Tk()
gui.geometry("290x150")

marco1=Frame(gui)
LPalabra=Label(marco1,text="Palabra")
EPalabra=Entry(marco1,width=15)
LPalabra.grid(row=0,column=0)
EPalabra.grid(row=0,column=1)

marco2=Frame(gui)
LPalabraMasLarga=Label(marco2,text="Palabra más larga")
EPalabraMasLarga=Entry(marco2,width=15)
LLongitud=Label(marco2,text="Longitud")
ELongitud=Entry(marco2,width=15)
LPalabraMasLarga.grid(row=0,column=0)
EPalabraMasLarga.grid(row=0,column=1)
LLongitud.grid(row=1,column=0)
ELongitud.grid(row=1,column=1)

BIngresar=Button(gui,text="Ingresar",command=ingresar)
BCalcular=Button(gui,text="Calcular",command=calcular)

marco1.pack()
BIngresar.pack()
BCalcular.pack()
marco2.pack()

gui.mainloop()
