import random

def situacao(lista):
    string = ""
    for i in lista:
        string += '{:<2} {}\n'.format(i[0],i[1])
    return string




lista_naipes = ["espadas","paus","copas","ouros"]
lista_numeros = [ i for i in range(1,14)]
cartas = []
for valor in lista_numeros:
    for naipe in lista_naipes:
        cartas.append([valor,naipe])
random.shuffle(cartas)


while True:
    jogada = input(situacao(cartas))
    print(len(cartas))
