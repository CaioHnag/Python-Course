dados = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    dados.append( [ nome, [ nota1 , nota2 ] ] )
    op = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while op not in ['S','N']:
        op = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if op == 'N':
        break
print(f'No   Aluno  Media')
print('-' * 30)
for i, lista in enumerate(dados):
    print(f'{i+1} {lista[0]} {( lista[1][0] + lista[1][1] ) / 2 }')
num = 0
while num != 999:
    print('-' * 30)
    num = int(input('Mostrar as notas de qual aluno? (999 para parar) : '))
    if num != 999:
        if num <= 0 or num > len(dados):
            while num <= 0 or num > len(dados):
                num = int(input('Digite as opções possiveis: '))
        print(f'Notas de {dados[num - 1 ][0]} == {dados[ num - 1 ][1]}')
        print('-' * 30)
        print()
print('Programa encerrado')