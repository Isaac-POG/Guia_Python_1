inversion = float(input("Ingrese la cantidad de inversion: "))
interes_anual = float(input("Ingrese el interes anual: "))
años = int(input("Ingrese la cantidad de años de inversion: "))

for i in range(años):
    inversion = int(inversion * (1 + interes_anual/100))
    print(f"El capital obtenido de la inversion es $ {inversion}")