numero_a_revisar = int(input("Ingrese un numero entero: "))

if(numero_a_revisar == 0 or numero_a_revisar == 1):
    print("El numero ingresado (0 o 1), por definicion no es ni PRIMO ni COMPUESTO.")
    exit(0)

if(numero_a_revisar < 0):
    numero_a_revisar *= -1
    print(f"El numero ingresado es negativo, se cambiara a un numero positivo: {numero_a_revisar}")
    
for i in range(1, numero_a_revisar):
    if(i != 1 and  numero_a_revisar % i == 0): break
    
if(i + 1 == numero_a_revisar):
    print(f"{numero_a_revisar} es PRIMO")
else:
    print(f"{numero_a_revisar} es COMPUESTO")