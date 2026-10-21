from time import sleep
def maior( *n ):
    print('Analisando os valores...')
    sleep(3)
    if len(n) != 0:
        mar = n[0]
        for valor in n:
            if valor > mar:
                mar = valor
    else:
        mar = 0
    print(f'No total são {len(n)} valores informados')
    sleep(1)
    print(f'O maior valor é { mar }')
maior()