import math
def triangul(a,b,c):
    if a<b+c and c<b+a and b<a+c:
        return True
    return False
a=float(input('MEDIDA:  '))
b=float(input('MEDIDA:  '))
c=float(input('MEDIDA:  '))
mr=max(a,b,c)
final=triangul(a,b,c)
print(final)
if final==True or final> mr:
    print('FORMARÁ UM TRIÂNGULO')
    if a != b != c:
        print('FORMARÁ UM TRIÂNGULO ESCALENO')
    elif a == b == c:
        print('FORMARÁ UM TRIÂNGULO EQUILATERO')
    else:
        print('FORMARÁ UM TRIÂNGULO ISOSCELES')
else:
    print('NÃO FORMARÁ UM TRIÂNGULO')
