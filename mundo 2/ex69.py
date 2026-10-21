mulheres = 0
homens = 0
pessoas = 0
while True:
    print('-=-=-=-=-=-=-=-=-=-=-=-=-')
    print('CADESTRE UMA PESSOA')
    print('-=-=-=-=-=-=-=-=-=-=-=-=-')
    sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
    while sexo not in 'MF' :
        sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
    idade = int(input('Digite a idade: '))
    while idade < 0:
        idade = int(input('Digite a idade: '))
    if idade > 18 :
        pessoas += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F':
        if idade < 18:
            mulheres += 1
    saida = str(input('Deseja continuar ? [S/N]: ')).strip().upper()[0]
    while saida not in 'SN':
        saida = str(input('Deseja continuar ? [S/N]: ')).strip().upper()[0]
    if saida == 'N':
        break
print(f'Foram cadastradas {pessoas} pessoas com mais de 18 anos.')
print(f'{homens} homens foram cadastrados')
print(f'{mulheres} mulheres tem menos de 18 anos.')