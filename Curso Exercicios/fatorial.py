#Faça um programa que leia um número qualquer e mostre o seu fatorial. 
#Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120
numero = int(input('Digite um numero: '))
fatorial = 1
for x in range(numero,0,-1):
    fatorial= fatorial * x
    print(f'{x} ', end='')
    print('x ' if x > 1 else '= ', end='')
print(fatorial)
