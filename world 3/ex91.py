from random import randint
from time import sleep
podio = dict()
final = {}
input()
for i in range(0,4):
    random = randint(1,10)
    lista = list()
    lista.append([f'jogador{i+1}' , random])
    sleep(1)
    print(f'Jogador {i+1} : {random}')
    podio[f'{i+1}'] = lista
mreserva = [0,0]
cont = 0
usados = []
while len(usados) != 4:
    for valor in podio:
        for nome , pontos in podio[valor]:
            if nome not in usados:
                if pontos > mreserva[1]:
                    mreserva = [nome, pontos]
    final[f'{cont + 1}'] = mreserva
    usados.append(mreserva[0])
    mreserva = [0,0]
    cont += 1
for valor in final:
        print(f'{valor} - {final[valor][0]} | {final[valor][1]} ')