#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
#No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
valores = list()
for x in range(0,5):
    valores.append(int(input(f'Digite o valor da posição {x}')))
print(f'O maior valor digitado foi {max(valores)} na posição: ',end='')
for c, i in enumerate(valores):
    if i == max(valores):
        print(f'{c+1}...', end='')
print(f'\nO menor valor digitado foi {min(valores)} na posição: ',end='')
for c, i in enumerate(valores):
    if i == min(valores):
        print(f'{c+1}...',end='')
print('\n',valores)
