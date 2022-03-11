#Escreva um programa em Python que leia um número inteiro qualquer 
#e peça para o usuário escolher qual será a base de conversão: 
#1 para binário, 2 para octal e 3 para hexadecimal.
numero = int(input())
print('Digite uma opção para coversao:\n[1] para binário\n[2] para octal\n[3] para hexadecimal')
opcao = int(input('Opcao: '))

if opcao == 1:
    print('{} para binário: {}',format(numero,bin(numero)))
elif opcao == 2:
    print('{} para octal: {}'.format(numero,oct(numero)))
elif opcao == 3:
    print('{} para hexadecimal: {}'.format(numero,hex(numero)))
else:
    print('Opcao inválida!')
