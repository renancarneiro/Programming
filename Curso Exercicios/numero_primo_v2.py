n = int(input())
contador = 0
for x in range(1,n+1):
    if n % x == 0:
        contador+=1
        print(f'Divisível por {x}')
    else:
        print(f'Não é divisivel por {x}')

if contador == 2:
    print('É numero primo')
else:
    print('Não é número primo')
