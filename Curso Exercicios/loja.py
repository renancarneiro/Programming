#Elabore um programa que calcule o valor a ser pago por um produto, 
#considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço formal 
# 3x ou mais no cartão: 20% de juros
preco = float(input())
print('Digite a forma de pagamento: ')
print('[1] Dinheiro/cheque')
print('[2] Cartão')
codigo = int(input())
desconto = 0
porcentagem = ''
preco_final = 0
if codigo == 1:
    desconto = preco * 0.10
    porcentagem = '10%'
    preco_final = preco - desconto
    
elif codigo == 2:
    print('Digite a opcao no cartão:\n[1] 2X no cartão: preco normal\n[2] 3X ou mais no cartão: 20% juros')
    op_cartao = int(input())
    if op_cartao == 1:
        porcentagem = 'Nenhum desconto'
        preco_final = preco
    elif op_cartao == 2:
        juros = preco * 0.20
        porcentagem = '20% de juros'
        preco_final = preco + juros
    else:
        print('Opcão inválida!')
else:
    print('Opção inválida!')

print('R${:.2f} com {} de desconto fica R${:.2f}'.format(preco, porcentagem, preco_final))
