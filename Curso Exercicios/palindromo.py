#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, 
#desconsiderando os espaços. Exemplos de palíndromos:
frase = input().upper()
frase = frase.split()
frase = ''.join(frase)
inverter = frase[::-1]
print(f'A frase invertida fica: {inverter}')
print(f'A frase original é: {frase}')

if frase == inverter:
    print('Essa frase é um palíndromo!')
else:
    print('Essa frase não é um palíndromo')
