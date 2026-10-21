from time import sleep
def cont(inicio , fim , passo):
    if passo == 0:
        passo = 1
    if inicio < fim :
        for i in range( inicio , fim + 1 , passo):
            print(i , end = ' ' )
            sleep(1)
    elif inicio > fim :
        for i in range( inicio , fim - passo, -passo):
            print(i , end = ' ')
            sleep(1)
    elif passo < 0:
        for i in range( inicio , fim + passo, passo):
            print(i , end = ' ')
            sleep(1)
    print('Fim')
print('Contagem de 1 até 10 , contando de 1 em 1: ')
for c in range( 1, 11):
    print(c , end = ' ')
    sleep(1)
print('Fim')
sleep(1)
print('Contagem de 1 até 10 , contando de 2 em 2: ')
for c in range( 1, 11 , 2):
    print(c , end = ' ')
    sleep(1)
print('Fim')
sleep(1)
print(f'Agora é sua vez , personalize a contagem.')
cont( int( input('Inicio: ') ) , int( input ('Fim: ') ), int( input ('Passo: ' ) ) )
