from funcoes_base import *
import random
#funcao principal que chama a intermediária e reinicia o jogo
def programa():
    inicio = "a"
    baralho = cria_baralho()
    random.shuffle(baralho)
    while inicio != "":
        inicio = input(regras)
    intermediario(baralho)

#funcao intermediaria que chama a si mesma, substituindo a necessidade de um loop para cada rodada
def intermediario(baralho):
        jogada = input(situacao(baralho))
        if pode_int(jogada):
            jogada = int(jogada)
            jogada_index = jogada-1
            if 1 <= jogada <= len(baralho) and len(lista_movimentos_possiveis(baralho,jogada_index)):
                jogada_index = jogada-1
                movimento = lista_movimentos_possiveis(baralho,jogada_index)[0]
                #parte de escolha sobre qual carta empilhar, se houver mais de uma carta disponivel para empilhar
                if len(lista_movimentos_possiveis(baralho,jogada_index)) > 1:
                    #função recursiva que se chama para evitar erros caso o jogador digite posição inválida
                    rec2(baralho,jogada_index)
                baralho = empilha(baralho,jogada_index,jogada_index-movimento)
                if not possui_movimentos_possiveis(baralho) and len(baralho) == 1:
                    print("Parabéns você ganhou")
                    programa()
                if not possui_movimentos_possiveis(baralho) and len(baralho) > 1 :
                    print("Você perdeu")
                    programa()
                else:
                    intermediario(baralho)
            else:
                print("Posição inválida. Por favor, digite um número entre 1 e 52.")
                intermediario(baralho)
        else:
            print("Posição inválida. Por favor, digite um número entre 1 e 52).")
            intermediario(baralho)

programa()
