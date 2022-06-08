edad = int(input("Ingrese su edad: "))
etapa = None
if 0<= edad <= 10:
    etapa = "La infancia es increible y bella"
elif 10< edad <=19:
    etapa = "Tienes muchos cambios, mucho que estudiar"
elif 19< edad <=29:
    etapa = "Amor y comienza el trabajo"
else:
    etapa = "No ingreso un numero valido"
print(f'Para el año {edad} corresponde la etapa: {etapa}')