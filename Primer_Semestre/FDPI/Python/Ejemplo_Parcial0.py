from tkinter import *


def tpg():
    if EUbi.get().lower() == "preferencial":
        if EFun.get() .lower()== "normal":
            Tpg = int(EBol.get()) * 17000
            ETot.delete(0, END)
            ETot.insert(0, Tpg)
        elif EFun.get().lower() == "3d":
            Tpg = int(EBol.get()) * 25000
            ETot.delete(0, END)
            ETot.insert(0, Tpg)
    elif EUbi.get().lower() == "general":
        if EFun.get().lower() == "normal":
            Tpg = int(EBol.get()) * 14000
            ETot.delete(0, END)
            ETot.insert(0, Tpg)
        elif EFun.get().lower() == "3d":
            Tpg = int(EBol.get()) * 19000
            ETot.delete(0, END)
            ETot.insert(0, Tpg)

gui = Tk()
gui.geometry("")
gui.resizable(False, False)
gui.title("Cine")
gui.config(height=30, width=30, bg="black")

m1 = Frame(gui, bg="black")
LUbi = Label(m1, text="Ubicación", font=("Arial", 12), bg="black", fg="white")
EUbi = Entry(m1, width=20, bd=3, bg="black", fg="white")
LUbi.grid(row=0, column=0)
EUbi.grid(row=0, column=1)
LFun = Label(m1, text="Tipo Función", font=("Arial", 12), bg="black", fg="white")
EFun = Entry(m1, width=20, bd=3, bg="black", fg="white")
LFun.grid(row=1, column=0)
EFun.grid(row=1, column=1)
LBol = Label(m1, text="Cantidad Boletos", font=("Arial", 12), bg="black", fg="white")
EBol = Entry(m1, width=20, bd=3, bg="black", fg="white")
LBol.grid(row=2, column=0)
EBol.grid(row=2, column=1)

m2 = Frame(gui, bg="black")
LTot = Label(m2, text="Total a pagar", font=("Arial", 12), bg="black", fg="white")
ETot = Entry(m2, width=20, bd=3, bg="black", fg="white")
LTot.grid(row=4, column=0)
ETot.grid(row=4, column=1)

BPg = Button(gui, text="Calcular Pago", font="Arial", command=tpg, bd=3, fg="white",bg="black")

m1.pack()
BPg.pack()
m2.pack()


gui.mainloop()
