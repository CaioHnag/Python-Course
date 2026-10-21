matriz = []
cont = 0
for i in range(0,3):
    a = int(input(f'Digite o valor [ {i} , {cont} ]: '))
    b = int(input(f'Digite o valor [ {i} , {cont + 1} ]: '))
    c = int(input(f'Digite o valor [ {i} , {cont + 2} ]: '))
    matriz.append([a, b, c])
for lista in matriz:
    print(f'{lista[0]}  |  {lista[1]}  |  {lista[2] }')
somapar = 0
for lista in matriz:
    for valor in lista:
        if valor % 2 == 0:
            somapar += valor
print(f'A soma dos valores pares são == {somapar}')
print(f'A soma da terceira coluna == {matriz[0][2] + matriz[1][2] + matriz[2][2]}')
print(f'O maior valor da segunda linha == {max(matriz[1])}')
