pessoas = []
while True:
    name = input("Nome: ").strip()
    pesos = int(input("Peso: "))
    pessoas.append([name, pesos])
    op = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if op == 'N':
        break
print(f'Foram digitados {len(pessoas)} pessoa(s)')
maior = pessoas[0][1]
menor = pessoas[0][1]
for lista in pessoas:
    if lista[1] >= maior:
            maior = lista[1]
    else:
        if lista[1] <= menor:
            menor = lista[1]
print('Maior peso : ', end = '')
for lista in pessoas:
         if lista[1] == maior:
           print(f'[ {lista[0]} == {lista[1]} ]', end = ' ')
print()
print('Menor peso: ',end = '')
for lista in pessoas:
    if lista[1] == menor:
        print(f'[ {lista[0]} == {lista[1]} ]', end = ' ')
