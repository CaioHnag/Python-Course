from random import randint
from time import sleep
palpites = []
quantidade = int(input('Quantos numeros você quer sortear?  '))
for i in range(0,quantidade):
    lista = []
    for num in range (0,6):
        a = randint(1,61)
        while a in lista:
            a = randint(1,61)
        lista.append(a)
    palpites.append(lista)
print(f'Sorteando os {quantidade} jogos...')
for indice , palpite in enumerate(palpites):
    sleep(1)
    print(f'Jogo {indice + 1} = {palpite}')
print('-=' * 10)
print('Boa Sorte!')
