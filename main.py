from llenar import crear_carta_laboral

cantidad = int(input("¿Cuantas cartas laborales desea crear? "))

for i in range (cantidad):
    cc = input("Ingrese el número de cedula del solicitante: ")
    salario = input("¿Desea incluir el salario?\n ingrese si o no: ").lower()
    
    if salario == "si":
        print(crear_carta_laboral(cc, True))
    else:
        print(crear_carta_laboral(cc, False))
