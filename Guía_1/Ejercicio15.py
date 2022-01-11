frase = input("Ingrese una frase: ")
letra = input("Ingrese una letra: ")
contador = 0   

for i in frase:
    if(i == letra):
        contador += 1
        
print(f"La letra {letra} se encuentra contenida en '{frase}', un total de {contador} veces.")