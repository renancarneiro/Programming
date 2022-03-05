tipo = input()
classe = input()
alimentacao = input()

if tipo == "vertebrado":
    if classe == "ave":
        if alimentacao == "carnivoro":
            print("aguia")
        else:
            print("pomba")
    else:
        if  alimentacao == "onivoro":
            print("homem")
        else:
            print("vaca")
        
else:
    if classe == "inseto":
        if alimentacao == "hematofago":
            print("pulga")
        else:
            print("lagarta")

    else:
        if alimentacao == "hematofago":
            print("sanguessuga")
        else:
            print("minhoca")
