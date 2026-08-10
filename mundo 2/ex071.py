cont50 = 0
cont20 = 0
cont10 = 0
cont1 = 0
valor = int(input('Valor a sacar:  '))
while True:
    if valor == 0:
        break
    if valor >= 50:
        cont50 += 1
        valor -= 50
    elif valor >= 20:
        cont20 += 1
        valor -= 20
    elif valor >= 10:
        cont10 += 1
        valor -= 10
    else:
        cont1 += 1
        valor -= 1
print(f'Foram usadas {cont50} notas de R$ 50,00')
print(f'Foram usadas {cont20} notas de R$ 20,00')
print(f'Foram usadas {cont10} notas de R$ 10,00')
print(f'Foram usadas {cont1} notas de R$ 1,00')
