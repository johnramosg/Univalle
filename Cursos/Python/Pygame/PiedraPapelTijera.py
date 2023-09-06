import random

i=1
victorias=0
derrotas=0
empates=0
while i==1:

  juego=input("Elija su opcion:\n1. Piedra\n2. Papel\n3. Tijera\nSu opción es: ")
  computadora=random.randrange(1,3)
  #Condicionales para realizar el juego
  if juego==1 and computadora==1:
    print("Ambos han legido piedra")
    empates+=1

  elif juego==1 and computadora==2:
    derrotas+=1
    print("Has perdido el rival ha elegido papel")

  elif juego==1 and computadora==3:
    victorias+=1
    print("Has ganado el rival eligio tijera")
  i=int(input("1.¿.Desea Jugar de Nuevo?\n2.¿Desea ver los resultados?\n3.Salir"))
  if i==2:
    print(f"Victorias: {victorias}\nEmpates:{empates}\nDerrotas{derrotas}")