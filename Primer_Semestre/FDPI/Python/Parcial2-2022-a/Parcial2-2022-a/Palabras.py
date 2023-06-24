from tkinter import *

def ingresar():
    print("Completar")
    
def calcular():
    print("Completar")
    
gui=Tk()
gui.geometry("300x150")

marco1=Frame(gui)
LPalabra=Label(marco1,text="Palabra ")
EPalabra=Entry(marco1,width=15)
LPalabra.grid(row=0,column=0)
EPalabra.grid(row=0,column=1)

BIngresar=Button(gui,text=" Ingresar palabra ",command=ingresar)
BCalcular=Button(gui,text=" Calcular ",command=calcular)

marco2=Frame(gui)
LCortas=Label(marco2,text="Palabras cortas")
ECortas=Entry(marco2,width=15)
LLargas=Label(marco2,text="Palabras largas")
ELargas=Entry(marco2,width=15)
LCortas.grid(row=0,column=0)
ECortas.grid(row=0,column=1)
LLargas.grid(row=1,column=0)
ELargas.grid(row=1,column=1)

marco1.pack()
BIngresar.pack()
BCalcular.pack()
marco2.pack()

gui.mainloop()
