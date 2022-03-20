#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
#Caso o número já exista lá dentro, ele não será adicionado. 
#No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
valores = []
while True:
    valores.append(int(input('Digite um numero: ')))
    x = len(valores)-1
    if valores[x] in valores[:-1]:
        print('Valor duplicado! não será cadastrado')
        del valores[x]
    else:
        print('Valor adicionado com sucesso!')
    continuar = input('Quer continuar? [S/N]').upper().strip()[0]
    while continuar not in 'SN':
        continuar = input('Inválido! Tente novamente\nQuer continuar? [S/N]').upper().strip()
    if continuar == 'N':
        break
print('Você digitou os valores: ',valores)
