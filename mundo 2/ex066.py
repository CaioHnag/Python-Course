cont = soma = 0
while True:
    n = int(input("Digite o número aqui:  "))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'Você digitou {cont} e a soma deles foi {soma}')
