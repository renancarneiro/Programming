#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1250,00, calcule um aumento de 10%. 
#Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input())
aumento = 0

if salario > 1250:
    aumento = (salario * 0.10) + salario
    porcentagem = '10%'
else:
    aumento = (salario * 0.15) + salario
    porcentagem = '15%'

print('O aumento do salario foi: R${:.2f}'.format(aumento))
print(f'A porcentagem foi: {porcentagem}')
