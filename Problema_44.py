# Problema 44: Calculadora basica con repeticion

while True:
    num1 = float(input('Ingrese el primer valor: '))
    num2 = float(input('Ingrese el segundo valor: '))
    suma = (num1 + num2)
    resta = (num1 - num2)
    mult = (num1 * num2)
    if num2 != 0:
        divi = (num1 / num2)
        mod = (num1 % num2)
    else:
        divi = None
        mod = None
    expo = (num1 ** num2)
    salir = False
    while True:
        calc = str(input('Que operacion desea calcular?: '))
        if calc in ['suma', 'Suma', 'SUMA']:
            print(suma)
            while True:
                repeti = str(input('Quiere realizar otra operacion?: '))
                if repeti.lower() in ['si', 'Si', 'SI']:
                    break
                elif repeti.lower() in ['no', 'No', 'NO']:
                    salir = True
                    break
                else:
                    print('Operacion no valida ingresar si o no')
            break
        elif calc in ['resta', 'Resta', 'RESTA']:
            print(resta)
            while True:
                repeti = str(input('Quiere realizar otra operacion?: '))
                if repeti.lower() in ['si', 'Si', 'SI']:
                    break
                elif repeti.lower() in ['no', 'No', 'NO']:
                    salir = True
                    break
                else:
                    print('Operacion no valida ingresar si o no')
            break
        elif calc in ['multiplicacion', 'Multiplicacion', 'MULTIPLICACION']:
            print(mult)
            while True:
                repeti = str(input('Quiere realizar otra operacion?: '))
                if repeti.lower() in ['si', 'Si', 'SI']:
                    break
                elif repeti.lower() in ['no', 'No', 'NO']:
                    salir = True
                    break
                else:
                    print('Operacion no valida ingresar si o no')
            break
        elif calc in ['division', 'Division', 'DIVISION']:
            print(divi)
            while True:
                repeti = str(input('Quiere realizar otra operacion?: '))
                if repeti.lower() in ['si', 'Si', 'SI']:
                    break
                elif repeti.lower() in ['no', 'No', 'NO']:
                    salir = True
                    break
                else:
                    print('Operacion no valida ingresar si o no')
            break
        elif calc in ['exponente', 'Exponente', 'EXPONENTE']:
            print(expo)
            while True:
                repeti = str(input('Quiere realizar otra operacion?: '))
                if repeti.lower() in ['si', 'Si', 'SI']:
                    break
                elif repeti.lower() in ['no', 'No', 'NO']:
                    salir = True
                    break
                else:
                    print('Operacion no valida ingresar si o no')
            break
        elif calc in ['modulo', 'Modulo', 'MODULO']:
            print(mod)
            while True:
                repeti = str(input('Quiere realizar otra operacion?: '))
                if repeti.lower() in ['si', 'Si', 'SI']:
                    break
                elif repeti.lower() in ['no', 'No', 'NO']:
                    salir = True
                    break
                else:
                    print('Operacion no valida ingresar si o no')
            break
        else:
            print('Operacion invalida favor de ingresar de nuevo')
    if salir:
        break
