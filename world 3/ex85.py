numeros = [ [] , [] ]
for i in range(0,7):
    num = input(f'Digite o valor {i + 1} : ')
    if int(num) % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)
numeros[0].sort()
numeros[1].sort()
print(f'Pares = {' - '.join( numeros[0] ) }')
print(f'Impares = {' - '.join( numeros[1] ) }')