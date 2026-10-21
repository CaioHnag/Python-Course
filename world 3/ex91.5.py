from random import randint
from time import sleep
podio = dict()
final = {}
input()
for i in range(0,4):
    random = randint(1,10)
    lista = list()
    lista.append(f'jogador{i+1}')
    lista.append(random)
    sleep(1)
    print(f'Jogador {i+1} : {random}')
    podio[f'{i+1}'] = lista
cont = 0
while cont != 4:
    for valor in podio:
        for value in podio:
            if valor != value:
                if podio[valor][1] > podio[value][1]:
                    podio[valor] , podio[value] = podio[value], podio[valor]
    cont += 1
for valor in podio:
    print(f'{valor} - {podio[valor][0]} | {podio[valor][1]}')