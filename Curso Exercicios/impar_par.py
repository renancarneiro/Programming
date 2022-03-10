#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
numero = int(input())

if numero % 2 == 0:
    print(f'{numero} é número par')
else:
    print(f'{numero} é número impar')
