#Crie um programa onde o usuário possa digitar sete valores numéricos 
#e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
#No final, mostre os valores pares e ímpares em ordem crescente.
unica = []
impar = []
par = []
for x in range(0,7):
    n = int(input(f'Digite o {x+1}º Valor:'))
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
par.sort()
unica.append(par[:])
par.clear()
impar.sort()
unica.append(impar[:])
impar.clear()
impar.sort()
par.sort()
print(f'Os valores pares digitados foram {unica[0]}\nOs valores impares digitados foram {unica[1]}')
