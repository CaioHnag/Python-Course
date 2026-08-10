import datetime
a=datetime.date.today().year
idade=int(input('ANO DE NASCIMENTO:   '))
final=a-idade
if final<=9:
    print('MIRIM')
elif final<=14:
    print('INFANTIL')
elif final<=19:
    print('JUNIOR')
elif final==20:
    print('SENIOR')
else:
    print('MASTER')


