calificacion = float(input("Ingrese la calificacion: "))
letra = None
if 9 <= calificacion <= 10:
    letra = "A"
elif 8 <= calificacion < 9:
    letra = "B"
elif 7 <= calificacion < 8:
    letra = "C"
elif 6 <= calificacion < 7:
    letra = "D"
elif 0 <= calificacion < 6:
    letra = "F"
else:
    letra = "No ingreso un numero valido"
print(f'Para la calificacion {calificacion} corresponde la nota: {letra}')