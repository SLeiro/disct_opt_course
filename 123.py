# coding=utf-8

import random
import pandas as pd
import os

my_dir = os.getcwd()
class maso(object):
    """Crea un maso de cartas españolas sin 8 y 9
    """
    def mezclado(self):
        values = ['1', '2', '3', '4', '5', '6', '7', '10', '11', '12']
        suites = ['Oro', 'Espada', 'Bastos', 'Copa']
        deck = [[v + ' of ' + s, v] for s in suites for v in values]
        length_of_deck = len(deck)
        cartas = []
        for card in range(length_of_deck):
            cartas.append(deck[card][1])
        return random.sample(cartas, len(cartas))



if __name__ == '__main__':
    cant_jugadas_acum = []
    cant_jugadas_gandas = 0
    cant_jugadas_perdidas = 0
    for x in range(1000000):
        deck = maso()
        mazo= deck.mezclado()
        v_decision = [1, 2,]
        i = 0
        j = 0
        jugadas = 0
        for carta in mazo:
            jugadas += 1
            if i == 2:
                i = 0
            if int(carta) == v_decision[i]:
                cant_jugadas_acum.append(jugadas)
                cant_jugadas_perdidas += 1
                break
            i += 1
            j += 1
            if j == 40:
                cant_jugadas_gandas += 1
    print(cant_jugadas_gandas, cant_jugadas_perdidas)
    df = pd.Series(cant_jugadas_acum)
    df.to_csv(os.path.join(my_dir,'salida_cant_jugadas'))



