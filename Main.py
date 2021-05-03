import funcoes_base as funcs
import random

def programa():
    inicio = "a"
    baralho = funcs.cria_baralho()
    random.shuffle(baralho)
    while inicio != "":
        inicio = input(regras)
    funcs.intermediario(baralho)

programa()


