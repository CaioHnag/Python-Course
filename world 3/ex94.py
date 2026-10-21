dados = list()
while True:
    a = str(input('Nome: '))
    b = str(input('Sexo: [M/F]: ')).upper()[0]
    while b not in 'MF':
        b = str(input('Sexo: [M/F]: ')).upper()[0]
    c = int(input('Idade: '))
    dados.append( {'Nome' : a , 'Sexo' : b ,  'Idade' : c} )
    op = str(input('Quer continuar? [S/N]: ')).upper()[0]
    while op not in 'SN':
        op = str(input('Quer continuar? [S/N]: ')).upper()[0]
    if op == 'N':
        break
print(dados)
qt = len(dados)
feminino = []
idade = []
acimamedia = []
print('-=' * 30)
print(f'{qt} pessoas foram registradas')
for item in dados:
    if item['Sexo'] == 'F':
        feminino.append(item['Nome'])
    idade.append(item['Idade'])
media = sum(idade) / qt
for item in dados:
    if item['Idade'] > media:
        acimamedia.append(item)
print(f'A media de idade é {round(media , 2)}')
print(f'As mulheres cadastradas foram : ' , end = ' ')
for valor in feminino:
    print(valor, end = ' ')
print()
print(f'As pessoas acima da media foram: ')
for item in acimamedia:
    print(item)
print('Programa encerrado!')