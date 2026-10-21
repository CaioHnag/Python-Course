lista = list()
op = 'S'
while op != 'N':
    user = int(input('Digite um valor:  '))
    lista.append(user)
    op = input('Deseja continuar? [S/N] ').strip().upper()[0]
    while op not in ['S', 'N']:
        op = input('Deseja continuar? [S/N] ').strip().upper()[0]
print(f'Foram digitados {len(lista)} números')
lista.sort(reverse=True)
print(f'Lista na ordem decrescente = {lista}')
if 5 in lista:
    print('Tem 5 na lista')
else:
    print('Não tem 5 na lista')
    