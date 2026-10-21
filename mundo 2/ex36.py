from time import sleep
cas=int(input('\033[1;35m QUAL O VALOR DA CASA DESEJADA? '))
sal=int(input('\033[1;35m SALARIO:  \033[m'))
parc=int(input('\033[1;35m QUANTOS ANOS:  \033[m'))
def parcelado(valor,anos):
    t=anos*12
    g=valor/t
    return g
def porcentagem(valor,quantosporcento):
    d=valor/10
    f=quantosporcento/10
    c=d*f
    return c
a=parcelado(cas,parc)
b=porcentagem(sal,30)
if b < a:
    print('\033[1;35m EMPRESTIMO NEGADO \033[m'.title())
elif b==a:
    sleep(3)
    print('EM ANALISE'.title())
    print('EMPRESTIMO PERMITIDO'.title())
else:
    sleep(3)
    print('PARABENS!!!!!'.title())
    print('EMPRESTIMO PERMITIDO'.title())
print(a)
print(b)

