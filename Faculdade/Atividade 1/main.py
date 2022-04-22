from caracter import Caracter
from time import sleep

caractere = Caracter(input('Digite um caractere: '))

opcoes = [1,2,3,4,5]
cont = 0

while True:
    cont+=1
    if cont > 1:
        sleep(4)
    print('=' * 24)
    print('   ESCOLHA UMA OPÇÃO!')
    print('=' * 24)
    print('1 - Quantidade de vogais\n2 - Inserir letra\n3 - Ocorrência da letra\n4 - Digitar novo caractere\n5 - Sair')
    opcao = int(input('Opção >> '))

    while opcao not in opcoes:
        print('Opção inválida')
        opcao = int(input('Opção >> '))

    if opcao == 1:
        res = caractere.qntd_vogal(caractere.char)
        print(f'A quantidade de vogais de "{caractere.char}" é "{res}"')

    elif opcao == 2:
        posicao = int(input(f'Posicão para inserir [0 até {len(caractere.char) - 1}]: '))
        posicoes = list(range(0, len(caractere.char)))
      
        while posicao not in posicoes:
            print('Posição inválida! Tente novamente')
            posicao = int(input(f'Posicao para inserir: [0 até {len(caractere.char) - 1}] '))
          
        subs = input('Inserir a letra: ').strip()[0]
        antigo = caractere.char
        caractere.inserir(caractere.char,posicao,subs)
        print(f'O caractere "{antigo}" ficou "{caractere.char}" com a modificação')

    elif opcao == 3:
        busca = input(f'Digite a letra para ocorrência: ')
        res = caractere.ocorrencia(caractere.char, busca)
        print(f'A ocorrência da letra "{busca}" em "{caractere.char}" é {res}')

    elif opcao == 4:
        caractere.char = input('Digite o novo caractere: ').strip()
        print(f'Caractere "{caractere.char}" cadastrado!')
      
    else:
        print('Programa finalizado! Volte sempre')
        break
