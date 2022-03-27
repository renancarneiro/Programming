#Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro 
#o ano de nascimento de uma pessoa, retornando um valor literal indicando 
#se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
def voto(ano):
    """
    => função que retorna a situação eleitoral de acordo com o ano 
       de nascimento informado.
       voto(ano) parametro 'ano'
    """
    from datetime import datetime
    situação = ''
    atual = datetime.now().year
    idade = atual - ano
    if idade > 17:
        if idade > 64:
            situação = 'OPCIONAL'
        else:
            situação = 'OBRIGATÓRIA'
    elif idade < 18 and idade >=16:
        situação = 'OPCIONAL'
    else:
        situação = 'NÃO VOTA'
    print(f'Você nasceu em {ano} sua idade é {idade} anos: {situação}')


ano = int(input('Ano de nascimento'))
voto(ano)
