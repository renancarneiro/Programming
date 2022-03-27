def fatorial(num, show=False):
    """
    Função fatorial 
    param => num: recebe um valor inteiro para calcular a fatorial
    param => show (opcional): se o usuario quiser ver o processo do calculo da fatorial
    """
    f = 1
    for x in range(num,0,-1):
        f = f * x
        if show == True:
            print(x, end=' ')
            if x > 1:
                print('x ', end='')
            else:
                print('= ', end='')
    print(f'{f}')
    
    
fatorial(6,True)
