# Declaracion de variables, son de tipo lista
tipo_pizza = input("Que tipo de Pizza comprara(Vegetariana o No vegetariana): ")
ingredientes_generales = ["Mozzarella", "Tomate"]
ingredientes_vegetarianos = ["Pimiento", "Tofu"]
ingredientes_no_veg = ["Peperoni", "Jamón", "Salmón"]
ingrediente_especial = "No se ingreso ninguna alternativa correcta"

# Diferencio entre tipo de pizzas o si no ingreso ninguna de las opciones
if(tipo_pizza == "Vegetariana"):
    # Muestro opciones
    print(ingredientes_vegetarianos)
    
    #Ingreso la opcion
    ingrediente_especial = input("¿Que ingrediente desea? ")
elif(tipo_pizza == "No vegetariana"):
    #Se repite lo mismo de arriba
    print(ingredientes_no_veg)
    ingrediente_especial = input("¿Que ingrediente desea? ")
else:
    #Si no se elige ninguna pizza se muestra un mensaje
    print(ingrediente_especial)
    
    #E indico que se finaliza el programa con exit
    exit(0)

#Al usar listas, con append puedo agregar un dato en la ultima posicion de la lista
ingredientes_generales.append(ingrediente_especial)

#Muestro el resultado
print(f"La pizza que deseo es {tipo_pizza} y sus ingredientes son {ingredientes_generales}")