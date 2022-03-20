#Crie um programa que vai ler vários números e colocar em uma lista. 
#Depois disso, crie duas listas extras que vão conter 
#apenas os valores pares e os valores ímpares digitados, respectivamente. 
#Ao final, mostre o conteúdo das três listas geradas.
numeros = []
pares = []
impares = []
while True:
    n = int(input('Digite um numero'))
    numeros.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    continuar = input('Quer continuar? [S/N]').upper().strip()[0]
    while continuar not in 'SN':
        continuar = input('Código inválido! Tente novamente\nQuer continuar? [S/N]').upper().strip()[0]
    if continuar == 'N':
        break
print(f'A lista completas dos numeros {numeros}')
print(f'A lista dos pares {pares}')
print(f'A lista dos impares {impares}')
