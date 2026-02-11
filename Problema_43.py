# Problema 43: Acumulador de abonos

abono = 0
while True:
    abonosuma = int(input('Ingrese la cantidad a abonar: '))
    if abonosuma < 0:
        print('Cantidad invalida vuelva a intentarlo')
    elif abono + abonosuma > 100000:
        print('La suma excede el limite de abono')
    else: 
        abono += abonosuma
        print('Su abono total es de $', abono)
        if abono >= 100000:
            print('Ha excedido el limite de $100,000 no se podra seguir abonando')
            break
        
