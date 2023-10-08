#Generar 50 numero aleatorios
rango_if=int(input('Introduzca Rango inferior :'))
rango_su=int(input('Introduzca Rango superior :'))

import random
from random import randint

numero = random.randint(rango_if,rango_su)
sumatot=0
sumimpar=0
sumpar=0
numeroif=rango_su
numerosup=rango_if
for c in range(50):
    if numero<=numeroif:
       numeroif=numero
    if numero>=numerosup:
       numerosup=numero
    print('numero :', numero)
    sumatot=sumatot+numero
    if (numero%2)==0:
        print('numero par:', numero)
        sumpar=sumpar+numero
    else: 
        print('numero impar:',numero)
        sumimpar=sumimpar+numero 
    numero = random.randint(rango_if,rango_su)

print('Total de suma de numeros:', sumatot)
print('Total de suma de numero impares:',sumimpar)
print('Total de Suma de numero pares:',sumpar)
print('Mayor numero:',numerosup)
print('Menor numero:',numeroif)


    
    