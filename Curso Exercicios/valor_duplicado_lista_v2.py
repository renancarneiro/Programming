#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
#Caso o número já exista lá dentro, ele não será adicionado. 
#No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
valores = []
while True:
    n = int(input('Digite um valor'))
    if n not in valores:
        valores.append(n)
        print('Valor cadastrado com sucesso!')
    else:
        print('Valor duplicado! Não será cadastrado')
    continuar = input('Quer continuar? [S/N]').upper().strip()[0]
    while continuar not in 'SN':
        continuar = input('Inválido, tente novamente!\nQuer continuar? [S/N]').upper().strip()[0]
    if continuar == 'N':
        break
print(f'Os valores digitados foram {valores}')
