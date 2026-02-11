# Problema 44: Calculadora basica con repeticion

while True:
    num1 = float(input('Ingrese el primer valor: '))
    num2 = float(input('Ingrese el segundo valor: '))
    suma = (num1 + num2)
    resta = (num1 - num2)
    mult = (num1 * num2)
    div = (num1 / num2)
    pot = (num1 ** num2)
    mod = (num1 % num2)
    print('suma: ', suma, 'resta:', resta, 'multiplicacion:', mult, 'division:', div, 'exponente:', pot, 'modulo:', mod)
    repetir = str(input('Quiere volver a hacer operaciones?: '))
    if repetir in ['si', 'Si', 'SI']:
        print('Continuaremos con las operaciones')
    elif repetir in ['no', 'No', 'NO']:
        print('No se continuara con las operaciones')
        break
