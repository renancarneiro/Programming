#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
#Não é divisivel por 2, 5, 7, 11

n = int(input())
if n==2 or n==5 or n==7 or n==11:
    print('Numero primo')
else:
    if n % 2 != 0 and n % 5 != 0 and n % 7 != 0 and n% 11 != 0:
        print('Número primo')
    else:
        print('Não é número primo')
