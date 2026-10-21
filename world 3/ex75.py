a = int(input('Número = '))
b = int(input('Número = '))
c = int(input('Número = '))
d = int(input('Número = '))
num = (a , b, c , d)
tr = num.index(3)
print(f'O número 9 apareceu {num.count(9)} vezes')
if tr == 0 :
    print('O número 3 não apareceu nenhuma vez')
else:
    print(f'O número 3 apareceu pela primeira vez na posição {tr + 1}')
print('Os valores pares digitados foram ' , end = '')
for valor in num :
    if valor % 2 == 0 :
        print(valor , end = ' ')
