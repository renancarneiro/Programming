#Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante
#‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
#Ex: n = leiaInt(‘Digite um n: ‘)
def leiaInt(msg):
    a = str(input(msg))
    while True:
        if a.isnumeric():
            a = int(a)
            break
        else:
            print('Entrada inválida, digite um numero')
            a = str(input(msg))
    print(f'Você acabou de digitar o nº {a}')
            
        
n = leiaInt('Digite um número: ')
