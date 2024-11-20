from utilities import *


def agregar_a_mesa(pilon_mesa: list, carta1, carta2):
    print("Es un empate, ambas cartas se guardan en el pilón de mesa.")
    agregar_cartas_a_mazo(pilon_mesa, carta1, carta2)
    


def transferir_cartas(ganador, carta1, carta2, mazo_jugadores, datos_jugadores):
    agregar_cartas_a_mazo(mazo_jugadores[ganador], carta1, carta2)
    print(f"{datos_jugadores[ganador]['nombre']} gana la ronda y recibe las cartas")

def incrementar_victorias_elementales(atributo_elegido, jugador, victorias_elemento):
    if atributo_elegido == "elemento":
        victorias_elemento[jugador] += 1

def resolver_empate(ganador, pilon_mesa, mazo_jugadores, datos_jugadores):
    if ganador == "jugador1":
        mazo_jugadores["jugador1"].extend(pilon_mesa)  
    else:
        mazo_jugadores["jugador2"].extend(pilon_mesa)  
    pilon_mesa.clear()  



def verificar_ganador_por_cartas(mazo_jugadores, datos_jugadores):
    if len(mazo_jugadores["jugador1"]) == 0:
        return "jugador2"  
    elif len(mazo_jugadores["jugador2"]) == 0:
        return "jugador1"  
    return None  

def ganador_ronda(resultado, carta1, carta2, datos_jugadores, mazo_jugadores, pilon_mesa, empate, victorias_elemento, atributo_elegido):
    if resultado == "Empate":
        agregar_a_mesa(pilon_mesa, carta1, carta2)
        return pilon_mesa, victorias_elemento


    if resultado == carta1:
        ganador = "jugador1"
    else:
        ganador = "jugador2"
    datos_jugadores[ganador]["puntuacion"] += 1
    transferir_cartas(ganador, carta1, carta2, mazo_jugadores, datos_jugadores)
    resolver_empate(ganador, pilon_mesa, mazo_jugadores, datos_jugadores)
    incrementar_victorias_elementales(atributo_elegido, ganador, victorias_elemento)
    return ganador, victorias_elemento, pilon_mesa



def determinar_ganador_final(datos_jugadores: dict, mazo_jugadores: dict, victorias_elementos) -> None:

    cartas_j1 = len(mazo_jugadores["jugador1"])
    cartas_j2 = len(mazo_jugadores["jugador2"])

    if victorias_elementos["jugador1"] >= 10:
        print(f"\n{datos_jugadores['jugador1']['nombre']} gana el juego con {victorias_elementos['jugador1']} victorias elementales!")
    elif victorias_elementos["jugador2"] >= 10:
        print(f"\n{datos_jugadores['jugador2']['nombre']} gana el juego con {victorias_elementos['jugador2']} victorias elementales!")
    # else:

    #     if cartas_j1 > cartas_j2:
    #         ganador = "jugador1"
    #     elif cartas_j2 > cartas_j1:
    #         ganador = "jugador2"
    #     else:
    #         print(f"\n¡Empate en el juego con {cartas_j1} cartas cada uno!")
    #         return
    #     print(f"\n{datos_jugadores[ganador]['nombre']} gana el juego con {len(mazo_jugadores[ganador])} cartas!")



    print(f"\nCartas finales:")
    print(f"{datos_jugadores['jugador1']['nombre']} tiene {cartas_j1} cartas.")
    print(f"{datos_jugadores['jugador2']['nombre']} tiene {cartas_j2} cartas.")



