contador = 0
soma = 0
for x in range(1,7):
    n = float(input())
    if n > 0:
        soma = soma + n
        contador = contador + 1

media = soma / contador 
print(f"{contador} valores positivos")
print("{:.1f}".format(media))
