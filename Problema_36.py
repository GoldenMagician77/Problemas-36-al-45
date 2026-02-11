# Problema 36: Repetir elevacion al cuadrado
        
num = int(input('Introduzca el numero a elevar al cuadrado: '))
cuad = (num ** 2)
print(cuad)
while True:
    repetir = input('Quieres elevar otro numero?: ')
    if repetir.lower() == 'si':
        num = int(input('Introduzca el numero a elevar al cuadrado: '))
        cuad = (num ** 2)
        print(cuad)
    elif repetir.lower() == 'no':
        print('Ha selecionado no. Adios.')
        break
    else:
        print('Opcion no valida introduzca si o no')
