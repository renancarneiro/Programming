#dados = list()
#copia = list()
#for x in range(0,4):
#    dados.append(input('Nome:').upper().strip())
#    dados.append(int(input('Idade:')))
#    copia.append(dados[:])
#    dados.clear()
#print(dados)
#print(copia)
dados = []
pessoas = []
maior = menor = 0
for x in range(0,3):
    pessoas.append(str(input('Nome:')).upper().strip())
    pessoas.append(int(input('Idade:')))
    dados.append(pessoas[:])
    pessoas.clear()
for p in dados:
    if p[1] < 18:
        print(f'{p[0]} tem {p[1]} anos, é menor de idade')
        menor+=1
    else:
        print(f'{p[0]} tem {p[1]} anos, é maior de idade')
        maior+=1
print(f'Tem {menor} menor de idade\nTem {maior} maior de idade')
