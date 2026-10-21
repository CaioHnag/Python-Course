salario=float(input('SALARIO:  '))
if salario >= 1250:
    a=salario//10
    b=salario+a
    print(f'VOCÊ TERÁ UM AUMENTO DE R${a}')
    print(f'VOCÊ FICARÁ COM SALARIO DE R${b}')
else:
    a=salario//10
    c=a//2
    d=a+c
    b=salario+a+c
    print(f'VOCÊ TERÁ UM AUMENTO DE R${d}')
    print(f'VOCÊ FICARÁ COM UM SALARIO DE R${b}')

