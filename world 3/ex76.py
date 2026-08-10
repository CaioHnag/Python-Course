produtos = ('Lapis' , 1.25 , 'Apontador' , 3.00 , 'Borracha' , 2.50 , 'Caderno' , 10.00 , 'Livro' , 54.50)
a = 0
b = 1
loop = 0
print('-=' * 20)
print('             VALORES')
print('-=' * 20)
while loop < len(produtos) / 2:
    loop += 1
    print(f'{produtos[a]}................. R$ {produtos[b]}')
    a += 2
    b += 2