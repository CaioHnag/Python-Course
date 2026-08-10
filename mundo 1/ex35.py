a=float(input("MEDIDA:   cm"))
b=float(input('MEDIDA:   cm'))
c=float(input('MEDIDA:   cm'))
d=min(a,c)
e=min(c,b)
f=max(a,b,c)
if d+e>f:
    print('PODE FORMAR UM TRIÂNGULO')
else:
    print("NAO PODE FORMAR UM TRIANGULO")

