#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e 
#cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, 
#o dicionário receberá também o ano de contratação e o salário. 
#Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import datetime
trabalhador = {}
trabalhador['nome'] = str(input('Nome:')).upper().strip()
ano = int(input('Ano de nascimento:'))
trabalhador['idade'] = datetime.now().year - ano
trabalhador['ctps'] = int(input('Nº CTPS [0 se não tiver]'))
if trabalhador['ctps'] != 0:
    trabalhador['contratação'] = int(input('Ano de contratação'))
    trabalhador['salario'] = int(input('Salário'))
print('-='*15)
trabalhador['aposentadoria'] = (trabalhador['contratação'] - ano) + 35
for k,v in trabalhador.items():
    print(f'{k}: {v}')
