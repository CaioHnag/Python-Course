num=int(input('NUMERO:  '))
total=0
for i in range(1,num+1):
     if num % i==0:
      print(f'\033[1;34m  {i}',end=' ')
      total+=1
     else:
      print(f'\033[1;31m  {i}',end=' ')
      total+=0
print(f'\n \033[1;36m O NUMERO FOI DIVISIVEL {total} vezes')
if total<=2:
    print('  É PRIMO  ')
else:
    print("  NÃO É PRIMO  ")

