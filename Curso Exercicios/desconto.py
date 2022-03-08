#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preco = float(input())
desconto = preco * 0.05
final = preco - desconto
print("O desconto de 5% sobre o valor de R$ {:.2f} é R${:.2f}\nPreço final: {:.2f}".format(preco,desconto,final))
