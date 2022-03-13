#Crie um programa que leia o ano de nascimento de sete pessoas. 
#No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
atual = date.today().year
maior = 0
menor = 0
for x in range(1,8):
    ano = int(input(f'{x}º'))
    idade = atual - ano
    if idade >=18:
        maior+=1
    else:
        menor+=1

print(f'Dentre as 7 pessoas há {maior} maior e {menor} menores')
