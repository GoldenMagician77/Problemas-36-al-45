# Problema 40: Repeticion con respuesta especifica

while True:
    besto = str(input('Ingrese su lenguaje de programacion favorito: '))
    if besto in ['Python', 'python', 'PYTHON']:
        break
    else:
        print('Ahora ingrese el de verdad')
