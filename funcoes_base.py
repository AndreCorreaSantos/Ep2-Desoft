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
def lista_movimentos_possiveis(baralho,indice):
    movs = []
    carta = baralho[indice]
    if indice-1 >=0:
        anterior = baralho[indice-1]
        if extrai_naipe(carta) == extrai_naipe(anterior) or extrai_valor(carta) == extrai_valor(anterior):
            movs.append(1)
    if indice-3 >=0:
        ter_anterior = baralho[indice-3]
        if extrai_naipe(carta) == extrai_naipe(ter_anterior) or extrai_valor(carta) == extrai_valor(ter_anterior):
            movs.append(3)
    return movs
def empilha(baralho,ori,dest):
    baralho[dest] = baralho.pop(ori)
    return baralho
