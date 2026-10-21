import time
dados = dict()
dados['nome'] = input('Digite seu nome:  ')
age = int(input('Digite seu ano de nascimento: '))
a = time.localtime()
dados['idade']= a.tm_year - age
dados['ctps'] = int(input('Digite sua carteira de trabalho(digite 0 se você não tem): '))
if dados['ctps'] == 0:
    print(f'Nome = {dados['nome']}')
    print(f'Idade = {dados['idade']}')
    print(f'CTPS = {dados['ctps']}')
else:
    dados['contratoano'] = int(input('Ano de contratação: '))
    dados['salario'] = int(input('Digite seu salario: R$'))
    dados['aposentadoria'] = dados['contratoano'] + 35 - a.tm_year + dados['idade']
    print(f'Nome = {dados['nome']}')
    print(f'Idade = {dados['idade']}')
    print(f'CTPS = {dados['ctps']}')
    print(f'Salario = {dados['salario']}')
    print(f'Aposentadoria = {dados["aposentadoria"]}')
