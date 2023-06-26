from tkinter import *

Cortas = list()
Largas = list()


def ingresar():
    if len(EP.get()) <= 8:
        Cortas.append(EP.get())
    elif len(EP.get()) > 8:
        Largas.append(EP.get())
    EP.delete(0, END)


def calcular():
    Cortas.sort()
    Largas.sort()
    EPC.delete(0, END)
    EPC.insert(0, Cortas)
    EPL.delete(0, END)
    EPL.insert(0, Largas)


gui = Tk()
gui.geometry("")
gui.title("Palabras cortas y largas")
gui.config(bg="black", borderwidth=0)
gui.resizable()

Marco1 = Frame(gui, bg="black")
LP = Label(Marco1, text="Palabra", bg="black", fg="white", font=("Times New Roman", 12))
EP = Entry(Marco1, width=30, borderwidth=0, bd=4, bg="gray")
LP.grid(row=0, column=0)
EP.grid(row=0, column=1)

Marco2 = Frame(gui, bg="black")
LPC = Label(
    Marco2, text="Palabras Cortas", bg="black", fg="white", font=("Times New Roman", 12)
)

EPC = Entry(Marco2, width=40, borderwidth=0, bd=4, bg="gray")
LPL = Label(
    Marco2, text="Palabras Largas", bg="black", fg="white", font=("Times New Roman", 12)
)
EPL = Entry(Marco2, width=40, borderwidth=0, bd=4, bg="gray")
LPC.grid(row=3, column=0)
EPC.grid(row=3, column=1)
LPL.grid(row=4, column=0)
EPL.grid(row=4, column=1)

BIP = Button(
    gui,
    text="Ingresar Palabra",
    command=ingresar,
    borderwidth=0,
    bd=4,
    font=("Times New Roman", 12),
    bg="gray",
)
BC = Button(
    gui,
    text="Calcular",
    command=calcular,
    borderwidth=0,
    bd=4,
    font=("Times New Roman", 12),
    bg="gray",
)

Marco1.pack()
BIP.pack()
BC.pack()
Marco2.pack()

gui.mainloop()
