#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
#Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
#A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
from time import sleep

valor_imovel = float(input('Valor imovel: R$'))
salario = float(input('Seu salario: R$'))
anos = int(input('Em quantos anos deseja pagar: '))

prestacao = valor_imovel / (anos * 12)
limite = salario * 0.3
print('Avaliando...')
sleep(3)

if prestacao > limite:
    print('NEGADO!')
    print('Limite de R${:.2f} excedido\nA prestacao da casa é: R${:.2f} de {}X'.format(limite,prestacao,anos*12))
else:
    print('Seu empréstimo foi aprovado! Parabéns!')
