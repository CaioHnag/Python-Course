from modulo import *
dados = dict()
cont = 0
while True:
    dicr = dict()                                           # { 1 : { nome ; partidas ;                                            #  gols     }  2  }
    dicr['Nome'] = str(input('Nome: '))
    dicr['Partidas'] = int(input('Partidas: '))
    gols = list()
    for i in range( dicr [ 'Partidas' ] ) :
        gols.append( int ( input( f'Gols na partidas {i + 1}:  ' ) ) )
    dicr['Gols'] = gols
    dados[f'{cont + 1}'] = dicr
    op = input('Deseja continuar? [S/N] ').strip().upper()[0]
    while op not in 'SN' :
        op = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if op == 'N':
        break
    cont += 1
print('-=' * 30)
tamanho = 0
indices = 0
l = []
for valor in dados:
    a = retornarcentro(len(valor), 9)
    b = retornarcentro(len(dados[valor]['Nome']), 16)
    c = retornarcentro(dados[valor]['Partidas'], 13)
    indices += 1
    tamanho = [a,b,c,b]
for valor in dados:
    l.append(returnlista(dados[valor]['Gols']))
tamanho.append(maximolista(l))
li = ['Cod','Nome','Partidas','Gols','Total']
print(f'{li[0] :<{tamanho[0]}}{li[1]:<{tamanho[1]}}{li[2]:<{tamanho[2]}}{li[3]:>{tamanho[3]}}{li[4]:>9}')
print('-=' * 30)
for dic in dados:
    print(f'{dic:<{tamanho[0]}}{dados[dic]['Nome']:<{tamanho[1]}}{dados[dic]['Partidas']:^{tamanho[2]}}{returnlista(dados[dic]['Gols']):^{tamanho[3]}}  {sum(dados[dic]['Gols']):>9}')
num = '0'
print('-=' * 30)
while True:
    num = input('Qual jogador você deseja saber os dados: COD -  ')
    if num == '999':
        break
    while int(num) <= 0 or int(num) > indices:
        num = input('Digite as possiveis opções: COD - ')
    print(f'Levantamento do jogador : {dados[num]["Nome"]}')
    print('-=' * 30)
    cont = 1
    for valor in dados[num]['Gols']:
        print(f'Partida {cont} = {valor}')
        cont += 1
    print('-=' * 30)
print('Obrigado por usar o programa')
