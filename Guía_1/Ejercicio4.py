# Declaraciones de variables
nombre = input("Ingrese su nombre: ")
repeticiones = int(input("Ingrese un numero entero: "))

# Utilizo el for para poder repetir x veces las palabras, indicando que range utilize 'repeticiones'
for i in range(repeticiones):
    print(f"{nombre}")