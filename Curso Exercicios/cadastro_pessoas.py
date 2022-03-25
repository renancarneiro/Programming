#Crie um programa que leia nome, sexo e idade de várias pessoas, 
#guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. 
#No final, mostre: 
#A) Quantas pessoas foram cadastradas 
#B) A média de idade 
#C) Uma lista com as mulheres 
#D) Uma lista de pessoas com idade acima da média
pessoa = {}
cadastros= []
while True:
    pessoa['nome'] = str(input('Nome:')).upper().strip()
    pessoa['sexo'] = str(input('Sexo [M/F]:')).upper().strip()[0]
    while pessoa['sexo'] not in 'MF':
        pessoa['sexo'] = str(input('Código Inválido! Tente novamente\nSexo [M/F]:')).upper().strip()
    pessoa['idade'] = int(input('Idade:'))
    continuar = str(input('Continuar? [S/N]')).upper().strip()[0]
    cadastros.append(pessoa.copy())
    pessoa.clear()
    while continuar not in 'SN':
        continuar = str(input('Código Inválido! Tente novamente\nContinuar? [S/N]')).upper().strip()[0]
    if continuar == 'N':
        break
soma = 0
for x in cadastros:
    soma+=x['idade']
media = soma/len(cadastros)
if len(cadastros) > 1:
    print(f'Foram cadastradas {len(cadastros)} pessoas')
else:
    print(f'Foi cadastrado {len(cadastros)} pessoa')
print(f'A media das idades foi: {media:.2f} anos')
print(f'As mulheres cadastradas foram:', end=' ')
for x in cadastros:
    if x['sexo'] == 'F':
        print(x['nome'], end=' | ')
print()
print(f'Lista das pessoas com idade acima da média:')
for x in cadastros:
    if x['idade'] > media:
        print(f' => nome: {x["nome"]} | sexo: {x["sexo"]} | idade: {x["idade"]}')
