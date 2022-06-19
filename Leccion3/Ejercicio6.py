print("Comprobamos que año es bisiesto")
opcion = 1
while opcion == 1:
    num = int(input("Ingrese año: "))
    condicion = ((num % 4 == 0) and (num % 100 != 0 ) or num % 400 == 0)

    if condicion:
        print("El año es bisiesto")
    else:
        print("El año no es bisiesto")

    opcion = int(input("Para seguir adelante digite la opcion 1: "))