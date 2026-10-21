dist=int(input('DISTÂNCIA EM KM\H:  '))
if dist<= 200:
    a=dist*0.50
    print(f'VALOR DA PASSAGEM: R${a}'.capitalize())
else:
    a=dist*0.45
    print(f'VALOR DA PASSAGEM: R$ {a}'.capitalize())

