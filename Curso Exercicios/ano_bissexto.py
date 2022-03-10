#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
#Caso 1) É um número divisível por 4, mas não é divisível por 100.
#Caso 2) É um número divisível por 4, por 100 e por 400.
ano = int(input())

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Ano bissexto!')
else:
    print('Não é bissexto!')
