a=int(input('DE QUE NUMERO VOCÊ QUER COMEÇAR:  '))
for i in range(1,52,2):
    print(i-1)
if a%2==0:
    for i in range(a+1,52,2):
       print(i)
else:
    for i in range(a-1,52,2):
        print(i)
