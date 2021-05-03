from funcoes_base 
import random

def programa():
    inicio = "a"
    baralho = cria_baralho()
    random.shuffle(baralho)
    while inicio != "":
        inicio = input(regras)
    intermediario(baralho)

programa()
