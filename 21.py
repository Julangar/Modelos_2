from random import shuffle
def baraja():
    return [(n, p) for n in (['A', 'J', 'Q', 'K']+[str(x) for x in range(2,11)]) for p in ['♠','♥','♣','♦']]

def mezclar(baraja):
    shuffle(baraja)
    return baraja

def sacar_carta(mazo):
    if mazo == []:
        pass
    else:
        print (mazo[0], valor_carta(mazo[0]))
        sacar_carta(mazo[1:])

def valor_carta(carta):
    if carta[0] in ['J','Q','K']:
        return 10
    elif carta[0] == 'A':
        return 1
    else:
        return int(carta[0])

def valor_mano(mano):
    if mano == []:
        return 0
    else:   
        return valor_carta(mano[0]) + valor_mano(mano[1:])

def valor_mano_recargado(mano):   
    if valor_mano(mano) <= 11 and 1 in [valor_carta(x) for x in mano]:
        return valor_mano(mano) + 10
    else:
        return valor_mano(mano)
def iniciar_juego(mazo, jugador, repartidor):
    jugar(mazo[4:], jugador+[mazo[0]]+ [mazo[1]], repartidor+[mazo[2]]+[mazo[3]])

def jugar(mazo, jugador, repartidor):
    print("Mano jugador: ",jugador) 
    print("Valor mano J: ", valor_mano_recargado(jugador))
    print("Mano repartidor: ","[Carta Oculata]", [repartidor[1:]])
    if len(mazo) > 2 and valor_mano_recargado(jugador)<21 and input("Pulse 'p' para sacar una carta, otra letra para plantarse ")=="p":
        jugar(mazo[1:], jugador+[mazo[0]], repartidor)
    else:
        print("Mano jugador: " + str(jugador))
        print("Valor mano J: ", valor_mano_recargado(jugador))
        repartir_repartidor(mazo, repartidor, jugador)

def repartir_repartidor(mazo,repartidor,jugador):
    if valor_mano_recargado(jugador) > 21 or valor_mano_recargado(jugador) <= valor_mano_recargado(repartidor):
        print("Mano repartidor: " + str(repartidor))
        print("Valor mano R: ", valor_mano_recargado(repartidor))
        ganador(valor_mano_recargado(jugador), valor_mano_recargado(repartidor))
    elif valor_mano_recargado(repartidor) < 21:
        repartir_repartidor(mazo[1:], repartidor+[mazo[0]], jugador)

def ganador(jugador, repartidor):
    if jugador > 21  :
        print('Gana el repartidor')
        return False
    elif repartidor >21:
        print('Gana el jugador')
        return False
    elif jugador > repartidor:
        print('Gana el jugador')
        return False
    else:
        print('Gana el repartidor')
        return False
    return True

iniciar_juego(mezclar(baraja()),[],[])
