cont = 0
soma = 0
termos = []
opcao = 's'
while opcao != 'n':
    usuario = int(input('Digite um valor:  '))
    cont += 1
    soma += usuario
    termos.append(usuario)
    opcao = str(input('Deseja continuar? [S/N]:  ')).strip().lower()
print(f'A media dos termos foi == {soma/cont}')
print(f'O maior termo foi == {max(termos)}\nMenor termo foi == {min(termos)}')
