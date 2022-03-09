#Faça um programa que leia um ângulo qualquer 
#e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
n = float(input())
sen= math.sin(math.radians(n))
cos = math.cos(math.radians(n))
tan = math.tan(math.radians(n))
print('sen({:.0f}) = {:.2f} \ncos({:.0f}) = {:.2f}\ntan({:.0f}) = {:.2f}'.format(n,sen,n,cos,n,tan))
