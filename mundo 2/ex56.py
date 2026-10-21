soma=0
mnr20=0
idh=[]
for tipo in range(0,4):
    nome=input('NOME:  ')
    idade=int(input('IDADE:  '))
    sexo=input('SEXO:   ').lower()
    soma+=idade
    if sexo=='feminino'and idade<20:
        mnr20+=1
    if sexo=='masculino':
        idh.append(idade)
        a=max(idh)
print(soma/4)
print(f'mulhered {mnr20}')
print(f'maior {max(idh)}')