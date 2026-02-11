# Problema 41: Confirmacion de contraseña (sin limite)

while True:
    contraseña = str(input('Ingrese una contraseña: '))
    confirmar = str(input('Vuelva a ingresar la contraseña: '))
    if confirmar == contraseña:
        print('Ambas contraseñas coinciden')
        break
    else:
        print('Las contraseñas no coinciden vuelva a intentarlo')
