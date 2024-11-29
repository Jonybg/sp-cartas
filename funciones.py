from utilities import *
from tateti import *

def agregar_a_mesa(pilon_mesa: list, carta1, carta2):
    print("Es un empate, ambas cartas se guardan en el pilón de mesa.")
    agregar_cartas_a_mazo(pilon_mesa, carta1, carta2)

def transferir_cartas(ganador, carta1, carta2, mazo_jugadores, datos_jugadores):
    agregar_cartas_a_mazo(mazo_jugadores[ganador], carta1, carta2)
    print(f"{datos_jugadores[ganador]['nombre']} gana la ronda y recibe las cartas")


def resolver_empate(ganador, pilon_mesa, mazo_jugadores, datos_jugadores):
    if ganador == "jugador1":
        mazo_jugadores["jugador1"].extend(pilon_mesa)
    else:
        mazo_jugadores["jugador2"].extend(pilon_mesa)
    pilon_mesa.clear()

def verificar_ganador_por_cartas(mazo_jugadores,datos_jugadores):
    ganador = None
    if len(mazo_jugadores["jugador1"]) == 0:
        ganador =  "jugador2"
    elif len(mazo_jugadores["jugador2"]) == 0:
        ganador =  "jugador1"
    return ganador

def verificar_ganador_por_rondas(mazo_jugadores,ronda,max_ronda):
    ganador = None
    if ronda == max_ronda:
        if len(mazo_jugadores["jugador1"]) > len(mazo_jugadores["jugador2"]):
            ganador = "jugador1"
        elif len(mazo_jugadores["jugador2"]) > len(mazo_jugadores["jugador1"]):
            ganador = "jugador2"
        else:
            ganador = "empate"
    return ganador
def ganador_ronda(resultado, carta1, carta2, datos_jugadores, mazo_jugadores, pilon_mesa, atributo_elegido):
    ganador = None

    if atributo_elegido == "elemento":
        resultado_tateti = jugar_tateti(carta1, carta2,datos_jugadores)  
        if resultado_tateti == "jugador1":
            ganador = "jugador1"
            datos_jugadores["jugador1"]["Victorias Elementales"] += 1  
        elif resultado_tateti == "jugador2":
            ganador = "jugador2"
            datos_jugadores["jugador2"]["Victorias Elementales"] += 1 
        else:
            ganador = "Empate"
    
    else:
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
            

    return ganador




