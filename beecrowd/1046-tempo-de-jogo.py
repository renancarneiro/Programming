inicial, final = input().split()
inicial = int(inicial)
final = int(final)

if inicial > final:
    horas = 24 - inicial + final

if inicial < final:
    horas = final - inicial 
    
if inicial == final:
    horas = 24

print(f"O JOGO DUROU {horas} HORA(S)")
