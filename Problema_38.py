# Problema 38: Validacion de numero entre 1 y 5

while True:
    num = int(input('Ingresa un numero entero del 1 al 5: '))
    if 1 <= num <= 5:
        print('Su numero ingresado es', num)
        break
    else:
        print('Numero no valido ingrese uno del 1 al 5 solamente')
