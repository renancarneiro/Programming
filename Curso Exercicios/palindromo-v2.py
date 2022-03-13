#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, 
#desconsiderando os espaços. Exemplos de palíndromos:
frase = input().upper()
frase = frase.split()
frase = ''.join(frase)
inverter = ''

for letra in range(len(frase)-1,-1,-1):
    inverter+= frase[letra]
print(f'Original: {frase}\nInvertida: {inverter}')
if frase == inverter:
    print('Essa frase é um palíndromo!')
else:
    print('Essa frase não é um palíndromo')
