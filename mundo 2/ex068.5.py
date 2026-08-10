from random import randint
print("-=" * 15)
print("Vamos jogar PAR ou IMPAR")
print("-=" * 15)
cont = 0
while True:
    jogador = input('Par ou Impar?  ').strip().upper()[0]
    while jogador not in 'PI':
        jogador = input('Par ou Impar?  ').strip().upper()[0]
    num = int(input("Escolha seu número agr:  "))
    while num > 11 or num < 0:
        num = int(input('Número fora dos limites:  '))
    computador = randint(0,10)
    soma = computador + num
    print(f'Eu escolhi {computador} você escolheu {num} a soma foi {soma}')
    if soma % 2 == 0 and jogador == 'P' :
        print('Parabéns você ganhou !')
        cont += 1
    elif soma % 2 != 0 and jogador == 'I':
        print('Parabéns você ganhou !')
        cont += 1
    else:
        print('Eu ganhei kkkkkkkkkk')
        break
print(f'Você ganhou {cont} vezes')