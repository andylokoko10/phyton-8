Rango_i=int(input('Introduzca rango inferior de la lista a Verificar Num Primos:' ))
Rango_s=int(input('Introduzca rango superior de la lista a Verificar Num Primos:' ))

print('Verificando que numero es primo o compuesto en el rango de:',Rango_i,' al :', Rango_s)
for i in range(Rango_i,Rango_s+1):

    
    EsPrimo=True
    if ((i%2==0) or (i%3==0) or (i%5==0)) and ((i!=2) and (i!=3) and (i!=5)):

        EsPrimo=False
        multiplo1=0
        multiplo2=0
        multiplo3=0
        cond=0
        cond1=0
        if (i%2==0):
            multiplo1=2
        if (i%3==0):
            if (multiplo1==0):
                multiplo1=3
            else:
                multiplo2=3
                cond=1
                cond1=1    
        if (i%5==0):
            if (multiplo1==0) and (multiplo2==0):
                multiplo1=5
            else:
                if cond1==1:
                   multiplo3=5
                else: 
                   multiplo2=5
                   cond=1

    
    if EsPrimo==True:
        print('El numero:',i,'Es Primo')
    else:
        if cond==0:
            print('El nmmero:',i,'Es Compuesto: al ser multiplo de : ', multiplo1)
        else:
            if (cond1==0)and (multiplo1!=0) and (multiplo2!=0):
                print('El nmmero:',i,'Es Compuesto: al ser multiplo de : ', multiplo1, 'y', multiplo2)
            else:
                if (cond1!=0) and  (multiplo3!=0):
                    print('EL numero:',i,'Es Compuesto: al ser multiplo de : ', multiplo1, multiplo2,'y',multiplo3)
