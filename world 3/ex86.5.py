matriz = [ [] , [] , [] ]
maior = 0
for lista in range(0,3):
    for c in range(0,3):
        matriz[lista].append(int(input(f'Digite o valor ({lista}, {c}) : ')))
        if len(str(matriz[lista][c])) > maior:
            maior = len(str(matriz[lista][c]))
for lista in matriz:
    print(f' {lista[0] :^{maior + 1}}  | {lista[1]:^{maior + 1}} |  {lista[2]:^{maior + 1}} ')
