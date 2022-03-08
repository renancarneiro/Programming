#Escreva um programa que converta uma temperatura 
#digitando em graus Celsius e converta para graus Fahrenheit.
#F = C * 1.8 + 32
celsius = float(input())
fahrenheit = celsius * 1.8 + 32
print('Os {:.2f}C em Fahrenheit é: {:.2f}F'.format(celsius,fahrenheit))
