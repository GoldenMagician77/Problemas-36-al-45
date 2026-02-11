# Problema 42:  Confirmacion de contraseña (con limite)

intentos = 0
while True:
    contraseña = str(input('Ingrese una contraseña: '))
    confirmar = str(input('Vuelva a ingresar la contraseña: '))
    if confirmar == contraseña:
        print('Ambas contraseñas coinciden')
        break
    else:
        print('Las contraseñas no coinciden vuelva a intentarlo')
        intentos += 1
        if intentos == 3:
            print('Ha excedido el limite de intentos por lo tanto su cuenta sera cancelada')
            break
        else:
            print('Intentos restantes: ', (3 - intentos))
