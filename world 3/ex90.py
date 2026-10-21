dados = dict()
dados['nome'] = input('Nome: ')
dados['media'] = float(input(f'Media de {dados["nome"]}:  '))
if dados['media'] >= 7:
    dados['situacao'] = 'Aprovado'
else:
    dados['situacao'] = 'Reprovado'
print(f'Seu nome é {dados["nome"]}.')
print(f'Sua media é {dados["media"]}.')
print(f'Sua situação é {dados["situacao"]}.')
