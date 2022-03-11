#Desenvolva um programa que leia o comprimento de três retas
#e diga ao usuário se elas podem ou não formar um triângulo
#(b - c) < a < (b + c)
#(a - c) < b < (a + c)
#(a - b) < c < (a + b)

a = float(input())
b = float(input())
c = float(input())

if (a-c) < a and a < (b+c):
    if (a-c) < b and b < (a+c):
        if (a-b)< c and c < (a+b):
            print('Pode formar um triangulo!')
        else:
            print('Não pode formar um triangulo')
