class Caracter:
  #Construtor
    def __init__(self, char):
        self.char = char

  #Funcao para contar a quantidade de vogais no caractere
    def qntd_vogal(self,frase):
        cont = 0
        lista_vogais = ['a','e','i','o','u']
        for x in frase:
            if x in lista_vogais:
                cont+=1
        return cont

  #Funcao para inserir uma letra na posicao do caractere
    def inserir(self, frase, posicao, caractere):
        frase = (' '.join(frase)).split()
        frase[posicao] = caractere
        self.char = ''.join(frase)

#Funcao para verificar a quantidade de occorência de determinada letra no caractere
    def ocorrencia(self,frase,procura):
        cont = 0
        for x in frase:
            if x == procura:
                cont+=1
        return cont
