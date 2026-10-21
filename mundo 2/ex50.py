soma=0
lista=[10,44,56,73,55,34,32]
for numero in lista:
    if numero%2==0:
        soma+=numero
    else:
        soma+=0
print(soma)