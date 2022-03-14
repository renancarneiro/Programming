n1 = int(input('Digite o nº 1'))
n2 = int(input('Digite o nº 2'))
codigo = 0
while codigo != 5:
    codigo = int(input('[1]somar\n[2]multiplicar\n[3]maior\n[4]novos números\n[5]sair do programa'))
    soma = n1 + n2
    multiplicar = n1 * n2
    maior = n1 
    if n2 > maior:
        maior = n2
    if codigo == 1:
        print(f'A soma dos dois valores é: {soma}')
    elif codigo ==2:
        print(f'O produto dos numeros é: {multiplicar}')
    elif codigo ==3:
        print(f'o maior entre os dois valores é: {maior}')
    elif codigo ==4:
        n1 = int(input('Digite o novo nº 1'))
        n2 = int(input('Digite o novo nº 2'))
    elif codigo ==5:
        break
    else:
        print('Opção inválida! Tente novamente')
print('Programa finalizado!')
