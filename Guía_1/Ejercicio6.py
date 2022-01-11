#Ingreso la fecha de cumpleaños
fecha_cumpleaños = input("Ingrese la fecha de cumpleaños en formato DD/MM/AAAA: ")

#Separo la fecha utilizando split e ingreso como delimitador el /, lo que me genera una lista
fecha_separada = fecha_cumpleaños.split("/")

#La muestro separada
print(f"Dia: {fecha_separada[0]}")
print(f"Mes: {fecha_separada[1]}")
print(f"Año: {fecha_separada[2]}")

