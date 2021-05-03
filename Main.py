from funcoes_base import cria_baralho,intermediario,regras
import random

def programa():
    inicio = "a"
    baralho = cria_baralho()
    random.shuffle(baralho)
    while inicio != "":
        inicio = input(regras)
    intermediario(baralho)

programa()
