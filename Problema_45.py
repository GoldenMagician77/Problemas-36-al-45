# Problema 45: Calculadora basica con repeticion por operacion

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
            resultado = suma
            print(resultado)
            igualvariable = calc
        elif calc in ['resta', 'Resta', 'RESTA']:
            resultado = resta
            print(resultado)
            igualvariable = calc
        elif calc in ['multiplicacion', 'Multiplicacion', 'MULTIPLICACION']:
            resultado = mult
            print(resultado)
            igualvariable = calc
        elif calc in ['division', 'Division', 'DIVISION']:
            resultado = divi
            print(resultado)
            igualvariable = calc
        elif calc in ['exponente', 'Exponente', 'EXPONENTE']:
            resultado = expo
            print(resultado)
            igualvariable = calc
        elif calc in ['modulo', 'Modulo', 'MODULO']:
            resultado = mod
            print(resultado)
            igualvariable = calc
        else:
            print('Operacion invalida favor de ingresar de nuevo')
            continue
        while True:
            repetir = str(input('Quiere repetir la misma operacion?: '))
            if repetir.lower() in ['si', 'Si', 'SI']:
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
                if igualvariable in ['suma', 'Suma', 'SUMA']:
                    resultado = suma
                elif igualvariable in ['resta', 'Resta', 'RESTA']:
                    resultado = resta
                elif igualvariable in ['multiplicacion', 'Multiplicacion', 'MULTIPLICACION']:
                    resultado = mult
                elif igualvariable in ['division', 'Division', 'DIVISION']:
                    resultado = divi
                elif igualvariable in ['exponente', 'Exponente', 'EXPONENTE']:
                    resultado = expo
                elif igualvariable in ['modulo', 'Modulo', 'MODULO']:
                    resultado = mod
                print(resultado)
                continue
            elif repetir.lower() in ['no', 'No', 'NO']:
                while True:
                    otra = str(input('Quiere realizar otra operacion?: '))
                    if otra.lower() in ['si', 'Si', 'SI']:
                        break
                    elif otra.lower() in ['no', 'No', 'NO']:
                        salir = True
                        break
                    else:
                        print('Operacion no valida ingresar si o no')
                if salir:
                    break
                break
            else:
                print('Operacion no valida ingresar si o no')
        if salir:
            break
    if salir:
        break
