a1=int(input('PRIMEIRO TERMO:  '))
a2=int(input('SEGUNDO TERMO:   '))
r=a2-a1
lista=[]
formula=a1+(10-1)*r
for numero in range(a1,formula,r):
    print(numero)
    lista.append(numero)
print(lista)