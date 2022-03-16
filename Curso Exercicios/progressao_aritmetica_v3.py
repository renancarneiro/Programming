p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
pa = p + (10 - 1) * r
x = p
n= 1
termos = 10
while x <= pa:
    x+=r
    print(x, end=' ')
while n != 0:
    x = p
    n = int(input('\nQuantos termos você quer mostrar?'))
    pa = p + (n - 1) * r
    termos+=n
    for y in range(0,n):
        x+=r
        print(x, end=' -> ')
    print('FIM')
print(f'\nProgressao encerrada com {termos} termos mostrados')
