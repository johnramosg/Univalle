def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b

def main():
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    print("¿Qué operación desea realizar?")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    opcion = int(input("Ingrese su opción: "))
    if opcion == 1:
        print("El resultado de la suma es:", suma(a, b))
    elif opcion == 2:
        print("El resultado de la resta es:", resta(a, b))
    elif opcion == 3:
        print("El resultado de la multiplicación es:", multiplicacion(a, b))
    elif opcion == 4:
        print("El resultado de la división es:", division(a, b))
    else:
        print("Opción incorrecta.")

if __name__ == "__main__":
    main()
