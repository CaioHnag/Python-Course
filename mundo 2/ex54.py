import datetime
data=datetime.date.today().year
jt=0
ns=0
for i in range(0,8):
    a=int(input('QUAL ANO VOCÊ NASCEU '))
    b=data-a
    if b>=18:
        print(f'\033[1;32m VOCÊ POSSUI MAIS DE 18 ANOS')
        jt+=1
    else:
        print('VOCE É MENIR DE IDADE')
        ns+=1
print(f'{jt} JÁ SAO MAIORES DE IDADE')
print(f'{ns} AINDA N SAO MAIORES DE IDADE')


