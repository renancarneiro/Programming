vendedor= input()
salario= float(input())
vendas= float(input())
comissao= vendas * 0.15
salario_final= comissao + salario
print("TOTAL = R$ {:.2f}".format(salario_final))
