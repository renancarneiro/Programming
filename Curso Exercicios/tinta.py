#Faça um programa que leia a largura e a altura de uma parede em 
#metros, calcule a sua área e a quantidade de tinta necessária 
#para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados
largura = float(input())
altura = float(input())
area = largura * altura
litro = area / 2
print(f'Largura {largura} x Altura {altura} = {area}M² \n A quantidade de tinta necessária é: {litro}L')

