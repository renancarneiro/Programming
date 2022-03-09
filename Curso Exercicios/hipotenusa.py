#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. 
#Calcule e mostre o comprimento da hipotenusa.
# c² = a² + b²
a = float(input())
b = float(input())
c = (a**2 + b**2) ** (1/2)
print('O comprimento da hipotenusa é: {:.2f}'.format(c))
#Pode usar o hypot da biblioteca math também
