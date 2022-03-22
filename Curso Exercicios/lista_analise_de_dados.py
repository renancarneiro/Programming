pessoas = []
dados = []
while True:
    pessoas.append(str(input('Nome:')).upper().strip())
    pessoas.append(float(input('Peso:')))
    dados.append(pessoas[:])
    pessoas.clear()
    continuar = input('Quer continuar? [S/N]').upper().strip()[0]
    while continuar not in 'SN':
        continuar = input('Código inválido! Tente novamente\nQuer continuar? [S/N]').upper().strip()[0]
    if continuar == 'N':
        break
maior = menor = 0
leves = list()
pesados = list()
for x, p in enumerate(dados):
    print(p)
    if x == 0:
        maior = p[1]
        pesados.append(p[0])
        menor = p[1]
        pesados.append(p[0])
    if p[1] > maior:
        pesados.clear()
        maior = p[1]
        pesados.append(p[0])
    elif p[1] == maior:
        pesados.append(p[0])
    if p[1] < menor:
        leves.clear()
        menor = p[1]
        leves.append(p[0])
    elif p[1] == menor:
        leves.append(p[0])
print(f'{len(dados)} pessoas foram cadastradas')
print(f'O menor peso foi {menor:.2f}KG de {leves}\nO maior peso foi {maior:.2f}KG de {pesados}')
