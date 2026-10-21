import random
al1= str(input(' ME DIGA O NOME DO ALUNO: '))
AL2= str (input( " ME DIGA O NOME DE UM ALUNO: "))
AL3= str (input ( ' ME DIGA O NOME DE UM ALUNO: '))
AL4= str ( input(' ME DIGA O NOME DE UM ALUNO: '))
lista= [ al1,AL2,AL3,AL4]
final=random.choice(lista)
print(f"' O aluno sorteado foi o aluno(a): \n '{final}")


