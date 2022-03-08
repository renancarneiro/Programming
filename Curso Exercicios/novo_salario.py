#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input())
novo = (salario * 0.15) + salario
print('Seu salario era: R${:.2f}\nSeu novo salário é: R$ {:.2f}'.format(salario,novo))
