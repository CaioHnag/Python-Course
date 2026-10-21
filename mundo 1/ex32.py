ano=int(input('QUAL ANO VOCÊ QUER SABER:  '))
if ano % 4 ==0 and ano% 400  == 0 :
    print('O ANO É BISSEXTO'.capitalize())
else:
    print('O ANO N É BISSEXTO'.capitalize())
