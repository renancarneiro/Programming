numero = int(input())

for n in range(1, numero+1):
    numero = int(input())
    
    if numero % 2 == 0:
        y= "EVEN"
    
    if numero % 2 != 0:
        y = "ODD"

    if numero > 0:
        x = "POSITIVE"
    if numero < 0:
        x = "NEGATIVE"

    if numero == 0:
        x = "NULL"
        print(f"{x}")
    else:
        print(f"{y} {x}")
