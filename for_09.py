base=float(input('Introducca la Base: '))
expo=int(input('Introduca el exponente :'))
base1=base
for x in range(expo):
    base1=base1*base1

print('La base de :',base, 'Elevado al Esponente :',expo, 'es igual a :', base1)

