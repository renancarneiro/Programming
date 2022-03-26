from time import sleep
def maior(*num):
    cont = maior = 0
    print('Análisando os valores passados...')
    sleep(1.5)
    while cont < len(num):
        for x in num:
            if cont == 0:
                maior = x
            else:
                if x > maior:
                    maior = x
            cont+=1
    print(f'Os valores foram {num}\nO maior valor é: {maior}')
    sleep(1)
maior(1,2,3,4,1,2000,3,222,3,55,53,2,10000,9)
