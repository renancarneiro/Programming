#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada Km acima do limite.
velocidade = float(input())
multa = 0
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('{}km... Limite excedido:\nMulta-> R${:.2f}'.format(velocidade,multa))
else:
    print('Tudo normal, pode seguir seu caminho!')
