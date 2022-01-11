from random import *

contraseña = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
              'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
              'w', 'x', 'y', 'z','0', '1', '2', '3', '4', '5', '6', 
              '7', '8', '9',]

contraseña_usuario = "abcdefghi"

for letra in enumerate(contraseña_usuario, 0):
    intento_letra = contraseña[randint(0, 35)]
    contraseña_usuario = str(intento_letra) + str(contraseña_usuario)

intento = ""

while(intento != contraseña_usuario):
    intento = ""
    
    for letra in enumerate(contraseña_usuario, 0):
        intento_letra = contraseña[randint(0, 35)]
        intento = str(intento_letra) + str(intento)
    print(intento)

print(f"La contraseña real era : {intento}")