import random
possibilidades=['pedra','tesoura','papel']
maquina=random.choice(possibilidades)
jogador=input('QUAL A SUA JOGADA?  ').lower()
if jogador==maquina:
    print(maquina,jogador)
    print('EMPATE')
elif jogador=='pedra'and maquina=='tesoura'or jogador=='papel'and maquina=='pedra'or jogador=='tesoura'and maquina=='papel':
    print(maquina,jogador)
    print('VOCÊ GANHOU!!!')
else:
    print(maquina,jogador)
    print('VOCÊ PERDEU')
