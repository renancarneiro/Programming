#Faça um programa que leia o peso de cinco pessoas. 
#No final, mostre qual foi o maior e o menor peso lidos
maior = 0
menor = 0
for x in range(0,5):
    peso = float(input())
    if peso > maior:
        maior = peso
    elif menor == 0:
        menor = peso
    elif peso < menor:
        menor = peso
print(f'O maior peso é: {maior}KG\ne o menor é {menor}KG')
