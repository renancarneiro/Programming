#Crie um programa que leia quanto dinheiro uma pessoa 
#tem na carteira e mostre quantos dólares ela pode comprar
n = float(input())
dolar = n / 5.06
print('A pessoa pode comprar $ {:.2f} com seus R$ {:.2f}'.format(dolar,n))
