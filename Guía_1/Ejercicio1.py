# Variables que ingresa el usuario
horas_trabajadas = int(input("Ingrese las horas de trabajos: "))
coste_x_hora = int(input("Ingrese el coste por hora: "))

# Variable para almacenar la paga
paga = horas_trabajadas * coste_x_hora

print(f"La paga de la persona es {paga}")