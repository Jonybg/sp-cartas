from utilities import *
from tateti import *

def agregar_a_mesa(pilon_mesa: list, carta1: dict, carta2: dict) -> None:
    '''Agrega las cartas a la mesa'''
    print("Es un empate, ambas cartas se guardan en el pilón de mesa.")
    agregar_cartas_a_mazo(pilon_mesa, carta1, carta2)

def transferir_cartas(ganador: str, carta1: dict, carta2: dict, mazo_jugadores: dict, datos_jugadores: dict) -> None:
    '''Transfiere las cartas al ganador e imprime el ganador de la ronda'''
    agregar_cartas_a_mazo(mazo_jugadores[ganador], carta1, carta2)
    print(f"{datos_jugadores[ganador]['nombre']} gana la ronda y recibe las cartas")

def resolver_empate(ganador: str, pilon_mesa: list, mazo_jugadores: dict) -> None:
    '''Transfiere las cartas del pilon de mesa al ganador de la ronda'''
    if ganador == "jugador1":
        mazo_jugadores["jugador1"].extend(pilon_mesa)
    else:
        mazo_jugadores["jugador2"].extend(pilon_mesa)
    '''Limpiamos el pilon de mesa'''
    pilon_mesa.clear()

def verificar_ganador_por_cartas(mazo_jugadores) -> str:
    '''Verifica si alguno de los jugadores ha quedado sin cartas
       retorna el ganador o None si no hay ganador'''
    ganador = None
    if len(mazo_jugadores["jugador1"]) == 0:
        ganador =  "jugador2"
    elif len(mazo_jugadores["jugador2"]) == 0:
        ganador =  "jugador1"
    return ganador

def verificar_ganador_por_rondas(mazo_jugadores: dict, ronda: int, max_ronda: int) -> str:
    '''Verifica cual de los dos jugadores tiene mas cartas al llegar a la ronda 250.
       retorna el ganador o empate si no hay ganador'''
    ganador = None
    if ronda == max_ronda:
        if len(mazo_jugadores["jugador1"]) > len(mazo_jugadores["jugador2"]):
            ganador = "jugador1"
        elif len(mazo_jugadores["jugador2"]) > len(mazo_jugadores["jugador1"]):
            ganador = "jugador2"
        else:
            ganador = "empate"
    return ganador
def verificar_victorias_elementales(datos_jugadores: dict) -> str:
    '''Verifica si alguno de los jugadores ha ganado 10 victorias elementales
       retorna el ganador o None si no hay ganador'''
    ganador = None
    for jugador in ["jugador1", "jugador2"]:
        if datos_jugadores[jugador]["Victorias Elementales"] >= 10:
            ganador = jugador
    return ganador

def ganador_ronda(resultado: str, carta1: dict, carta2: dict, datos_jugadores: dict, mazo_jugadores: dict, pilon_mesa: list, atributo_elegido: str) -> str:
    '''Devuelve el ganador de la ronda
       retorna el ganador o None si no hay ganador'''
    ganador = None
    '''Si el atributo elegido es elemento vamos a la funcion para resolverlo'''
    if atributo_elegido == "elemento":
        resolver_elemento(carta1, carta2, datos_jugadores)
    else:
        '''Si hay empate, transferimos las cartas al pilon de mesa'''
        if resultado == "Empate":
            agregar_a_mesa(pilon_mesa, carta1, carta2)
            '''Si no hay empate, transferimos las cartas al ganador'''
        elif resultado == "carta1":
            ganador = "jugador1"
        elif resultado == "carta2":
            ganador = "jugador2"
        '''Con el ganador aumentamos la puntuacion, transferimos las cartas al ganador y resolvemos el empate (si hay)'''
        if ganador:  
            datos_jugadores[ganador]["puntuacion"] += 1
            transferir_cartas(ganador, carta1, carta2, mazo_jugadores, datos_jugadores)
            resolver_empate(ganador, pilon_mesa, mazo_jugadores)
            

    return ganador




