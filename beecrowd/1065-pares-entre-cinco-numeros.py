contador = 0
for x in range(1,6):
    n = int(input())
    if n % 2 == 0:
        contador = contador + 1
print(f"{contador} valores pares")
