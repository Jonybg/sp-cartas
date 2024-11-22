from utilities import *

def agregar_a_mesa(pilon_mesa: list, carta1, carta2):
    print("Es un empate, ambas cartas se guardan en el pilón de mesa.")
    agregar_cartas_a_mazo(pilon_mesa, carta1, carta2)

def transferir_cartas(ganador, carta1, carta2, mazo_jugadores, datos_jugadores):
    agregar_cartas_a_mazo(mazo_jugadores[ganador], carta1, carta2)
    print(f"{datos_jugadores[ganador]['nombre']} gana la ronda y recibe las cartas")

def incrementar_victorias_elementales(atributo_elegido, jugador, datos_jugadores):
    if atributo_elegido == "elemento":
        datos_jugadores[jugador]["Victorias Elementales"] += 1

def resolver_empate(ganador, pilon_mesa, mazo_jugadores, datos_jugadores):
    if ganador == "jugador1":
        mazo_jugadores["jugador1"].extend(pilon_mesa)
    else:
        mazo_jugadores["jugador2"].extend(pilon_mesa)
    pilon_mesa.clear()

def verificar_ganador_por_cartas(mazo_jugadores, datos_jugadores):
    ganador = None
    if len(mazo_jugadores["jugador1"]) == 0:
        ganador =  "jugador2"
    elif len(mazo_jugadores["jugador2"]) == 0:
        ganador =  "jugador1"
    return ganador

def ganador_ronda(resultado, carta1, carta2, datos_jugadores, mazo_jugadores, pilon_mesa, atributo_elegido):
    
    ganador = None
    if resultado == "Empate":
        agregar_a_mesa(pilon_mesa, carta1, carta2)
    elif resultado == "carta1":
        ganador = "jugador1"
    elif resultado == "carta2":
        ganador = "jugador2"
    if ganador:  
        datos_jugadores[ganador]["puntuacion"] += 1
        transferir_cartas(ganador, carta1, carta2, mazo_jugadores, datos_jugadores)
        resolver_empate(ganador, pilon_mesa, mazo_jugadores, datos_jugadores)
        incrementar_victorias_elementales(atributo_elegido, ganador, datos_jugadores)

    return ganador




