#Ingresar 10 notas, si el usuario ingresa una nota no valida se detiene el ingreso.
for x in range(10):
    nota = float(input('Ingresar nota ',str(x+1),': '))
    if nota < 0 or nota > 20:
        print('Nota no valida')
        break