dados = dict()
dados['nome'] = str(input('Nome: '))
dados['Partidas'] = int(input('Partidas: '))
lista = list()
for i in range(1, dados['Partidas'] + 1):
   gol = int(input(f'Quantos gols na partida {i}: '))
   lista.append(gol)
dados['gols'] = lista
print(dados)
print('-=' * 20)
print(f'O campo nome é {dados["nome"]}')
print(f'O campo partidas é {dados["Partidas"]}')
print(f'O campo gols é { sum( dados["gols"] ) }')
print('-=' * 20)
print(f'O jogador {dados["nome"]} jogou {dados["Partidas"]} partidas')
for indice , valor in enumerate(dados['gols']):
    print(f'Na partida {indice +1} = {valor} gols')
print(f'Foi um total de { sum(dados["gols"]) } gols')
