from random import randint
num = (randint(1,10) ,   randint (1 ,10) , randint(1 ,10) , randint(1 ,10) , randint (1,10) )
for numer in num :
    print(numer , end = ' ')
print()
print(f'O maior número é {max(num)}')
print(f'O menor número é {min(num)}')
