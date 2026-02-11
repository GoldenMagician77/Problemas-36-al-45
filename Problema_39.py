# Problema 39: Continuar con confirmacion

while True:
    simon = str(input('Quieres continuar?: '))
    if simon in ['si', 'Si', 'SI']:
        print('Ok continuamos')
    else:
        break
