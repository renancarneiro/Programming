#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a 
#quantidade de dias pelos quais ele foi alugado. 
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
# km / dias / dia * 60 / km * 0.15 / precoKM + precoDIAS
km = int(input())
dias = int(input())
precoKM = km * 0.15
precoDIAS = dias * 60
preco = precoDIAS + precoKM
print(f'Foram {km}km durante {dias} dias')
print(f'O preço pelos km rodados é: R$ {precoKM}\nO preço pelos dias é: R$ {precoDIAS}\nPreço final: R$ {preco}')

