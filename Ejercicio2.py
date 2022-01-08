# Declaro una variable para utilizar posteriormente
n = -1

# Encierro el input en un while, para que de esta forma, el usuario
# se vea obligado en ingresar un entero positivo (1 a inf+)
while(n < 1):
    n = int(input("Ingrese un entero positivo: "))
    
# Hago el calculo, le coloco int para que indique unicamente enteros
suma = int(n*(n+1)/2)

#Muestro el resultado
print(f"El resultado de la suma de todos los enteros de 1 a {n} es de {suma}")