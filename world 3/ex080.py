lista = [ 0 ]
for i in range(1 , 6) :
    a = int(input(f'Digite um valor : ')) # PEDE O VALOR AO USUÁRIO.
    if a >= max (lista) : #TESTA SE O VALOR É MAIOR QUE O MAIOR VALOR ATUAL DA LISTA.
        lista.insert( lista.index ( max( lista ) ) + 1, a )  # SE FOR REAL A POSIÇÃO A FRENTE DO MAIOR VALOR ATUAL , RECEBE O NOVO MAIOR VALOR.
        if i == 1 : # SE FOR A PRIMEIRA VEZ DO USARIO DIGITANDO .
            lista.remove( 0 )   # SE DER VERDADEIRO, ELE REMOVE O ZERO QUE ESTAVA NA LISTA, POIS ESTE N FOI UM NÚMERO DIGITADO PELO USÁRIO.
        print('Valor adicionado na ultima posição.')
    elif a >= min (lista) : # TESTA SE O VALOR DO USARIO É MAIOR OU IGUAL AO MENOR VALOR ATUAL DA LISTA.
        print('1')
        b = 0
        for valor in lista: # SE O TESTE DER VERDADEIRO, O PROGRAMA TESTARÁ CADA VALOR NA LISTA.
            if valor >= a:  # SE O VALOR FOR MAIOR OU IGUAL AO VALOR ATUAL QUE FOI TESTADO, QUER DIZER QUE ENTÃO ESSE VALOR ESTÁ NA FRENTE DO VALOR DIGITADO.
                b = valor   # VARIAVEL B , RECEBE O VALOR QUE VAI ESTAR NA FRENTE
                break   # ELE QUEBRA O LOOP , POIS ENTÃO ESTE SERÁ O MENOR VALOR QUE VAI ESTAR NA FRENTE DO USARIO.
        print(f'Valor adicionado na posição {lista.index ( b ) }') # DIZ QUE O VALOR DIGITADO FOI COLOCADO NA ANTIGA POSIÇÃO DO MENOR VALOR QUE É MAIOR DO QUE O VALOR DIGITADO.
        lista.insert( lista.index ( b )  , a) # EXECUTA O PROCESSO
    elif a < min (lista) : # TESTA SE O VALOR DIGITADO É MENOR QUE O MENOR VALOR ATUAL.
        print('2')
        print(f'Valor adicionado na posição 0') # A MENOR POSIÇÃO NA LISTA SEMPRE SERÁ 0
        lista.insert( 0 , a) # ADICIONA O VALOR NA MENOR POSIÇÃO POSSIVEL
print(lista)