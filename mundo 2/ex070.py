total = 0
maiorq = 0
maisbarato = ''
pr = 0
loop = 0
print('-=' * 20)
print('LOJAS HNAGSSS')
print('-=' * 20)
while True:
    loop += 1
    nome = input('Nome do produto: ').upper()
    precor = float(input('Preço do produto: R$'))
    preco = round(precor,2)
    total += preco
    if loop == 1:
        maisbarato = nome
        pr = preco
    if preco > 1000:
        maiorq += 1
    if preco < pr:
        maisbarato = nome
        pr = preco
    saida = str(input('Deseja continuar? ')).strip().upper()[0]
    while saida not in 'SN':
        saida = str(input('Deseja continuar? ')).strip().upper()[0]
    if saida == 'N':
        break
print('=' * 20)
print('VALORES FINAIS')
print('=' * 20)
print(f'TOTAL = R${total}')
print(f'{maiorq} produtos custam mais de R$1000.00')
print(f'O produto mais barato foi {maisbarato} que custou R${pr}')
