while True:
    conta = input('Digite a expressão: ').strip()
    lista = list(conta)
    if '(' in lista or ')' in lista:
        abertos = 0
        for valor in lista:
            if valor == '(':
                abertos += 1
            elif valor == ')':
                abertos -= 1
            if abertos < 0:
                break
        if abertos == 0:
            print('Sua expressão é valida')
        else:
            print('Sua expressão não é valida')
    else:
        print('Não há parenteses na conta')
    op = input('Deseja continuar? [S/N] ').strip().upper()[0]
    while op not in ['S', 'N']:
        op = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if op == 'N':
        break
print('Obrigado por usar o programa')