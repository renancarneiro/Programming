times = ('America-mg','athletico-pr','atlético-go','atlético-mg','avaí','botafogo','ceará SC',
        'corinthians','coritiba','cuiabá','flamengo','fluminense','fortaleza','goiás','internacional',
        'juventude','palmeiras','bragantino','santos','são paulo')
print(f'Lista de times do campeonato brasileiro {times}')
print('=' * 100)
print('5 primeiros',times[:5])
print('=' * 100)
print('4 ultimos',times[-4:])
print('=' * 100)
print('Ordem alfabética',sorted(times))
print('=' * 100)
posicao = times.index('botafogo')
print(f'Posição do time do botafogo: {posicao+1}º')
