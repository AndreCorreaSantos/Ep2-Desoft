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

def possui_movimentos_possiveis(baralho):
    for indice in range(0,len(baralho)):
        if len(lista_movimentos_possiveis(baralho,indice)) > 0:
            return True
    return False

regras = "Paciência Acordeão \n seja bem vindo(a) ao jogo de Paciência Acordeão! O objetivo deste jogo é  colocar todas as cartas em uma mesma pilha. \n Existem apenas dois movimentos possíveis \n 1. Empilhar uma carta sobre a carta imediatamente anterior \n 2. Empilhar uma carta sobre a terceira carta anterior. \n Para que um movimento possa ser realizado basta que uma das duas condições abaixo seja atendida: \n 1. As duas cartas possuem o mesmo valor ou \n 2. As duas cartas possuem o mesmo naipe. \n Desde que alguma das condições acima seja satisfeita, qualquer carta pode ser movimentada. \n Aperte [ENTER] para iniciar o jogo..."

#função para testar se string pode virar inteiro, evitar erros
def pode_int(string):
    try:
        int(string)
        return True
    except:
        return  False

    #recebe um baralho e retorna uma string formatada para ser imprimida na tela do jogador
def situacao(baralho):
    string = ""
    for carta in baralho:
        string += '{}. {}{}\n'.format(baralho.index(carta)+1,extrai_valor(carta),extrai_naipe(carta))
    string = "O Estado atual do baralho é: \n {} \n Escolha uma carta (digite um número entre 1 e {}):   ".format(string,len(baralho))
    return string

#funcao para fazer o display dos movimentos e a formatacao da string da escolha entre empilhar sobre a primeira carta ou sobre a terceira
def escolha(lista,jogada):
    jogada = lista[jogada]
    return "Sobre qual carta você quer empilhar o {}{}? \n 1.{}{} \n 2.{}{} \n".format(extrai_valor(jogada),extrai_naipe(jogada),extrai_valor(lista[lista.index(jogada)-1]),extrai_naipe(lista[lista.index(jogada)-1]),extrai_valor(lista[lista.index(jogada)-3]),extrai_naipe(lista[lista.index(jogada)-3]))
#funcao para mostrar as cartas que o usuario pode empilhar (caso haja mais que uma) e que chama a si mesma caso o usuario digite uma posição errada
def rec2(baralho,jogada_index):
    esc = input(escolha(baralho,jogada_index))
    if esc == "1":
        return lista_movimentos_possiveis(baralho,jogada_index)[0]
    if esc == "2":
        return lista_movimentos_possiveis(baralho,jogada_index)[1]
    else:
        print("Posição inválida, por favor digite 1 ou 2.")
        rec2(baralho,jogada_index)
