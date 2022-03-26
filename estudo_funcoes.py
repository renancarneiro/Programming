def mensagem(msg):
    print('-='*15)
    print(msg)
    print('-='*15)

def soma(*num): #pega os varios numeros de um parametro e coloca em uma tupla
    print(f'A soma de todos os valores é: {sum(num)}')
    
def maior(*num):
    print(f'O maior numero é: {max(num)}')

def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos]*=2
        pos+=1

        
#uso da funcao soma dos parametros
soma(1,5,10)
#uso da funcao maior entre os numeros do parametro
maior(1,3,5,3,10,1,12,10)
#uso da funcao mensagem
mensagem('TESTE')
#uso da funcao dobra
valores = [2,3,1,4,5,10]
dobra(valores)
print(valores)
