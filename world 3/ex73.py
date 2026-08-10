times = ('palmeira','flamengo','atletico-pr','fluminense','cruzeiro','bahia','corinthians','bragantino','botafogo','coritiba','atletico-mg','são paulo ', 'vitotia','gremio','mirassol','internacional','santos','vasco','remo','chapecoense')
for pos , time in enumerate(times) :
    if pos == 5:
        break
    print(f'\033[1;34m{pos+1} = {time.capitalize()}\033[m')
print()
print('\033[1;31mZ4\033[m')
print('-=' * 20)
for pos , time in enumerate(times) :
    if pos >= len(times) - 4:
        print(f'\033[1;31m {pos+1} = {time.capitalize()}\033[m')
print('-=' * 20)
for time in sorted(times) :
    print(f'{time[0].upper()} = {time.capitalize()}')
print('-=' * 20)
for  pos , time in enumerate(times) :
    if time == 'chapecoense':
        print(f'{pos+1} = {time.capitalize()}')

