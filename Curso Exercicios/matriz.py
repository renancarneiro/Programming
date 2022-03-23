matriz=[[],[],[]]
soma = terceira = 0
maior = []
for x in range(0,3):
    for i in range(0,3):
        matriz[x].append(int(input(f'Digite o valor da [{x},{i}]')))
for x in range(0,3):
    for i in range(0,3):
        print(f'[{matriz[x][i]:^5}]', end='')
        if matriz[x][i] % 2 == 0:
            soma+=matriz[x][i]
        if i == 2:
            terceira+=matriz[x][i]
    print()
print(f'A soma dos pares é: {soma}\nA soma dos valores da terceira coluna é {terceira}')
print(f'O maior valor da segunda linha é: {max(matriz[1])}')

