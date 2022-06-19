
mes = int(input("Ingrese el mes del año que desea consultar: "))
estacion = None
if 1>= mes <= 3:
    estacion = "Verano"
elif 4>= mes <=6:
    estacion = "Otoño"
elif 7>= mes <=9:
    estacion = "Invierno"
elif 10>= mes <=12:
    estacion = "Verano"
else:
    estacion = "No ingreso un numero valido"
print(f'Para el mes {mes} corresponde la estacion: {estacion}')