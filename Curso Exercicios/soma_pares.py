#Desenvolva um programa que leia seis números inteiro
#e mostre a soma apenas daqueles que forem pares. 
#Se o valor digitado for ímpar, desconsidere-o.
soma = 0
contador = 0
for x in range(1,7):
    numero = int(input(f'Digite {x}º numero'))
    if numero % 2 == 0:
        contador+=1
        soma+= numero
print(f'Soma dos {contador} numeros é {soma}')
