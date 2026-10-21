numero= int(input("\033[1;34m NUMERO: \033[m"))
fechar='\033[m'
if numero%2==0:
    print(f'\033[1;36m PAR {fechar}'.capitalize())
else:
    print(f'\033[1;33m IMPAR {fechar}'.capitalize())
