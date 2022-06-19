suma = 0
calificacionBaja = 99999

for i in range(0,10):
    calificacion = int(input("Digite una calificación " + str(i+1) + ": "))
    suma = suma + calificacion
    if calificacion < calificacionBaja:
        calificacionBaja = calificacion

calificacioPromedio = suma / 10
print(f"""La calificación promedio es: {calificacioPromedio}
La calificacion mas baja es: {calificacionBaja}""")
