num = ('zero', 'um' , 'dois' , 'três' ,'quatro' , 'cinco' , 'seis' , 'sete' , 'oito' , 'nove' , 'dez' , 'onze' , 'doze' , 'treze' , 'quatorze' , 'quinze' , 'dezesseis' , 'dezessete' , 'dezoito', 'dezenove', 'vinte')
user = int(input('Digite um número de 0 a 20 : '))
while user > 20 or user < 0:
    user = int(input('Digite um número de 0 a 20 :  '))
print(f'O número é {num[user].capitalize()}')

