# Problema 37: Interes compuesto con repeticion

C = int(input('Introduzca la capital inicial: '))
i = int(input('Introduzca la tasa de interes: '))
n = int(input('Introduzca el numero de periodos: '))
M = (C * (1 + i) ** n)
print('El monto final es de ', M)
while True:
    repetir = input('Quiere hacer otro calculo?: ')
    if repetir == 'si':
        C = int(input('Introduzca la capital inicial: '))
        i = int(input('Introduzca la tasa de interes: '))
        n = int(input('Introduzca el numero de periodos: '))
        M = (C * (1 + i) ** n)
        print('El monto final es de ', M)
    elif repetir == 'no':
        print('No se realizaran mas calculos')
        break
    else:
        print('Opcion no valida introduzca si o no')
