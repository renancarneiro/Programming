salario = float(input())

if salario <= 400.00:
    reajuste = salario * 0.15
    salario = salario + reajuste
    porcentagem = "15 %"
    
elif salario >= 400.01 and salario <= 800:
    reajuste = salario * 0.12
    salario = salario + reajuste
    porcentagem = "12 %"
    
elif salario >= 800.01 and salario <=1200:
    reajuste = salario * 0.10
    salario = salario + reajuste
    porcentagem = "10 %"
    
elif salario >= 1200.01 and salario <=2000:
    reajuste = salario * 0.07
    salario = salario + reajuste
    porcentagem = "7 %"
    
elif salario > 2000:
    reajuste = salario * 0.04
    salario = salario + reajuste
    porcentagem = "4 %"
    
print("Novo salario: {:.2f}".format(salario))
print("Reajuste ganho: {:.2f}".format(reajuste))
print(f"Em percentual: {porcentagem}")
