#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
#A) Quantos números foram digitados.  
#B) A lista de valores, ordenada de forma decrescente.     
#C) Se o valor 5 foi digitado e está ou não na lista.
numeros = []
while True:
    numeros.append(int(input('Digite um valor')))
    continuar = input('Quer continuar? [S/N]').upper().strip()[0]
    while continuar not in 'SN':
        continuar = input('Código inválido! Tente novamente\nQuer continuar? [S/N]').upper().strip()[0]
    if continuar == 'N':
        break
print(f'Valores digitados: {numeros}\nVocê digitou {len(numeros)} elementos')
numeros.sort(reverse=True)
print(f'Valores de forma decrescente {numeros}')
if 5 in numeros:
    print('O valor 5 está na lista')
else:
    print('O valor 5 não está na lista')
