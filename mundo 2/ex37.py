from time import sleep

num=int(input('\033[1;34m NUMERO:  \033[m'))
print('\033[1;35m PARA QUAL BASE VOCÊ DESEJA CONVERTER:\n [1] BINARIO \n [2]OCTAL \n [3] HEXADECIMAL\033[m')
choice=int(input('\033[1;37m ESCOLHA:  \033[m'))
if choice==1:
    a=bin(num)
    b=a[2:]
    print('CONVERTENDO...')
    sleep(3)
    print(f'\033[1;34m O NUMERO COM ESTE TIPO DE BASE É \n {b}\033[m')
elif choice==2:
    c=oct(num)[2:]
    print('CONVERTENDO...')
    sleep(3)
    print(f'O NUMERO COM ESTE TIPO DE BASE É \n {c}')
elif choice==3:
     f=hex(num)[2:]
     print('CONVERTENDO...')
     sleep(3)
     print(f'O NUMERO CONVERTIDO PARA ESTA BASE É \n {f}')
else:
    print('ERRO')