#Crie um programa que leia o nome e o preço de vários produtos. 
#O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.
cont = total = cont_1000 = barato = 0
produto_barato = ' '
while True:
    continuar = 'X'
    nome = input('Nome do produto:').upper().strip()
    preco = float(input('Preço do produto:'))
    total+=preco
    cont+=1
    if preco > 1000:
        cont_1000+=1
    if barato == 0:
        barato = preco
    if preco < barato:
        barato = preco
        produto_barato = nome
    while continuar not in 'SN':
        continuar = input('Você quer continuar? [S/N]').strip().upper()[0]
    if continuar == 'N':
        break
print(f'Compra finalizada!\n[{cont}] Produtos -> Total gasto: R${total:.2f}\n{cont_1000} produtos custam mais de R$1000')
print(f'O produto mais barato é o {produto_barato} que custou R${barato:.2f}')
