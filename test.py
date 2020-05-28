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


def jugar(mazo, jugador, repartidor):
    print("Mano jugador: ",jugador,"Mano repartidor: ",repartidor) 
    print("Valor mano J: ", valor_mano_recargado(jugador)," Valor mano R: ", valor_mano_recargado(repartidor))
    if len(mazo) > 2 and valor_mano_recargado(jugador)<21 and valor_mano_recargado(repartidor)<21:
        jugar(mazo[2:], jugador+[mazo[0]], repartidor+[mazo[1]])


def ganador(jugar, jugador, repartidor):
    if valor_mano_recargado(jugador) <= 21 and valor_mano_recargado(repartidor) < valor_mano_recargado(jugador):
        print('Gana el jugador')
    elif valor_mano_recargado(jugador) >21 or valor_mano_recargado(jugador)<valor_mano_recargado(repartidor):
        print('Gana el repartidor')

def play(mazo, jugador):
    print("Se jugara el juego 21 contra la maquina:")
    print("Mano jugador: ",jugador) 
    print("Valor mano J: ", valor_mano_recargado(jugador))
    print("¿Desea pedir otra carta? Si(1), No(2)")
    if len(mazo) > 2 and valor_mano_recargado(jugador)<21:
        play(mazo[2:], jugador+[mazo[0]])
        
    
#sacar_carta(mezclar(baraja()))
#print (mezclar(baraja()))
#print (valor_mano_recargado(mezclar(baraja())[:2]))
#jugar(mezclar(baraja()),[],[])
#play(mezclar(baraja()),[])