sexo = str(input('Sexo:   ')).lower()
while sexo not in 'fm':
    sexo = str(input('Sexo invalido , digite novamente:  '))
print('Sexo verificado')
