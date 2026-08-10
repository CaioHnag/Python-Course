import random
import time
a=random.randint(0,5)
palp=int(input('\033[1;36m TENTE ADIVINHAR O NUMERO:  \033[m'.capitalize()))
print('\033[1;36m PROCESSANDO... \033[m')
time.sleep(3)
if palp== a:
    print('\033[7;32m VOCE ACERTOU!!\033[m')
else:
    print('\033[7;31m VOCE ERROU!!!\033[m')
print('\033[4;33m SE QUISER TENTAR DE NOVO REINICIE O PROGRAMA!! \033[m')

