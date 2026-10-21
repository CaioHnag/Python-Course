cont = 0
nu = 1
while True:
    cont = 0
    nu = 1
    print("Digite um número negativo para sair")
    n = int(input('Digite um número aqui para saber sua tabuada: '))
    if n < 0:
        break
    for num in range (1,11) :
        print(f'{n} x {num} = {n*num}')
print("Obrigado por usar o programa")
