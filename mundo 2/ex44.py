valor=float(input('VALOR:  '))
mp=input('MEIO DE PAGAMENTO:  '.title()).lower()
if mp=='cartão':
    vezes=int(input('QUANTAS VEZES SERÁ FEITA?  '))
    if vezes==1:
     df=valor-(valor/10)/2
     print(f'VOCÊ PAGARÁ R${df}')
    elif vezes>=3:
        fd=((valor/10)*2)+valor
        print(f'VOCÊ PAGARÁ R${fd}')
    else:
         print(f'VOCÊ PAGARÁ R${valor}')
if mp=='dinheiro'or mp=='a vista':
    sd=valor-(valor/10)
    print(f'VOCÊ PAGARÁ R${sd}')



