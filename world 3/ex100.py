from random import randint
from time import sleep
def sorteio(lista):
    for i in range (0, 5):
        sort = randint(1, 100)
        lista.append(sort)
        print(sort , end = ' ')
        sleep(1)
    print()
def somapar(lista):
    soma = 0
    for num in lista:
        if num % 2 == 0:
            soma += num
    print(f'A soma dos números pares = {soma}')
a = []
input('Clique aqui para sortear os números: ')
sorteio(a)
somapar(a)
