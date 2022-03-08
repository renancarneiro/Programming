#Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.
n = int(input())
for x in range(1,11):
    print(f'{x} * {n} = {x*n}')
