#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.
numeros = (int(input('Digite um valor')),
            int(input('Digite outro valor')),
            int(input('Digite mais um valor')),
            int(input('Digite o ultimo valor')))
print(f'Os numeros digitados foram {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O numero 3 apareceu na {numeros.index(3)+1}º posição')
else:
    print('O numero 3 não foi digitado em nenhuma posição')
print(f'Os numeros pares digitados foram: ',end='')
cont = 0
for x in numeros:
    if x % 2 == 0:
        print(x, end=' ')
        cont+=1
if cont == 0:
    print('Nenhum numero par foi digitado',end='')
