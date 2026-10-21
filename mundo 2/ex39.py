import datetime
a=int(input('QUAL ANO VOCÊ NASCEU'.title()))
sexo=input('QUAL SEU SEXO?  '.title()).lower()
b=datetime.date.today().year
c=b-a
d=18-c
i=abs(d)
if sexo=='masculino':
    if d==0:
        print('JÁ ESTÁ NA HORA DE SE ALISTA!!!')
    elif c<18:
        print(f'FALTA {i} anos para vocé se alistar')
    elif c>18:
        print(f'ja passou {i} anos de seu alistamento')
    else:
        print('end')
else:
    print('VOCÊ N TEM OBRIGAÇAO EM SE ALISTAR')
print(b)