vel=int(input('\033[1;34m VELOCIDADE DO CARRO EM KM\H: \033[m'))
if vel <= 80:
    print('\033[1;32m TUDO CONFORME , NÃO LEVARÁ MULTA \033[m')
else:
    a=vel*7-80*7
    print('\033[1;31m VOCÊ ESTÁ ACIMA DO LIMITE DE VELOCIDA DE 80km\h \033[m')
    print(f'\033[1;36m VOCÊ LEVOU UMA MULTA DE R${a} \033[m')


