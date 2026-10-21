matriz = []
contador = 0
for i in range( 0 , 3 ):
    a = input(f'Digite um valor [{i} , {contador }] : ')
    b = input(f'Digite o valor [{i} , {contador + 1}] : ')
    c = input(f'Digite o valor [{i} , {contador + 2}] : ')
    matriz.append([a, b, c])
for lista in matriz:
    print(f'{ lista[0]}  |  {lista[1]}  |  {lista[2] }')
