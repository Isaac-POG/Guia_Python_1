#Declaro variable de tipo cadena
numero_telefono = input("Ingrese el numero de telefono(Ejemplo: +34-913724710-56): ")

#Separo la cadena usando la funcion split y delimitador "-", y lo almaceno en otra variable, generando una lista
lista_separado = numero_telefono.split("-")

#Muestro el resultado, la casilla que necesitamos de la lista es 1
print(f"El telefono de la persona es : {lista_separado[1]}")