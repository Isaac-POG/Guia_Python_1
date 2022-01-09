#Declaracion de variables
edad_persona = int(input("Ingrese su edad: "))
ingresos_mensuales = int(input("Ingrese sus ingresos mensuales: "))

#Segun los datos entregados, me muestra la informacion que necesito
if(edad_persona > 15):
    if(ingresos_mensuales > 1000):
        print("Usted tiene que pagar impuestos")
    else:
        print("No tiene que pagar impuestos, porque sus ingresos son muy bajos")
else:
    print("No tiene que pagar impuestos, porque es muy joven")