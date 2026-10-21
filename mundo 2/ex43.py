altura=float(input('QUAL A SUA ALTURA:  '))
peso=float(input('QUANTO VOCÊ PESA:  '))
cr=peso/(altura*altura)
ap=round(cr,2)
print(ap)
if ap<18.5:
    print('ABAIXO DO PESO,PROCURE UM MEDICO!!!')
elif ap>=18.5 or ap<=25:
    print("PESO IDEAL")
elif ap>25 or ap<=30:
    print('SOBREPESO')
elif ap>30 or ap<=40:
    print('OBESIDADE')
else:
    print('OBESIDADE MORBIDA')

