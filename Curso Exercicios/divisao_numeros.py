#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
numero = int(input())
n1 = numero//1%10
n2 = numero//10%10
n3 = numero//100%10
n4 = numero//1000%10
print(f'Unidade: {n1}')
print(f'Dezena: {n2}')
print(f'Centena: {n3}')
print(f'Milhar: {n4}')
