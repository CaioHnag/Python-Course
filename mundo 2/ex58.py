import random
computador = random.randint(0,10)
jogador = int(input('Qual o seu palpite:   '))
chances = 1
while jogador != computador:
    chances += 1
    if jogador < computador:
        print('Valor maior')
    else:
        print('Valor menor')
    jogador = int(input('Palpite errado tente novamente: '))
print(f'Voce acertouuu\nPalpites == {chances}')
