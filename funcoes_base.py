def cria_baralho():
    lista_naipes = ["♠","♥","♣","♦"]
    lista_numeros = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    baralho = []
    for valor in lista_numeros:
        for naipe in lista_naipes:
            baralho.append("{}{}".format(valor,naipe))
    return baralho
def extrai_valor(carta):
    return carta[0:-1]
def extrai_naipe(carta):
return carta[-1]

