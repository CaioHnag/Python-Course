usuario = 0
soma = 0
cont = 0
while usuario != 999:
    usuario = int(input('Digite um número:  '))
    if usuario == 999:
        break
    soma += usuario
    cont += 1
print(f'Soma = {soma}')
print(f'Valores digitados = {cont}')
