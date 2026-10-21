lista = list()
for i in range( 0 , 5 ):
    a = int(input(f'Digite um valor para posição {i}: '))
    lista.append(a)
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {max(lista)} nas posições ' , end = ' ')
for indice , item in enumerate(lista):
    if max(lista) == item:
        print(f'{indice}...', end = ' ')
print()
print(f'O menor valor digitado foi { min(lista) } nas posições ' , end = ' ')
for indice , item in enumerate(lista):
    if item == min(lista):
        print(f'{indice}...', end = ' ')