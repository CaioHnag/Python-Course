import random
n= str(input('ME DIGA O NOME DO ALUNO: '))
n2=str( input(' ME DIGA O NOME DO ALUNO: '))
n3= str( input( 'ME DIGA O NOME DO ALUNO: '))
n4= str ( input( 'ME DIGA O NOME DO ALUNO: '))
lista=[n,n2,n3,n4]
random.shuffle(lista)
print(f'a ordem sorteada foi ')
print(lista)



