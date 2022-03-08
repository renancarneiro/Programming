segundos= int(input())

minutos = segundos//60
segundos= segundos%60
horas = minutos //60
minutos = minutos - (horas * 60)

print(f"{horas}:{minutos}:{segundos}")
