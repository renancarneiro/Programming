codigo, qntd, valor= input().split()
codigo2, qntd2, valor2= input().split()
codigo = int(codigo)
qntd = int(qntd)
valor = float(valor)
codigo2 = int(codigo2)
qntd2 = int(qntd2)
valor2 = float(valor2)

preco1=qntd*valor
preco2=qntd2*valor2
total= preco1+preco2

print("VALOR A PAGAR: R$ {:.2f}".format(total))
