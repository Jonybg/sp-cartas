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
    pilon_mesa = []

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
    if resultado == "carta1":
        ganador = "jugador1"
    else:
        ganador = "jugador2"
    

    datos_jugadores[ganador]["puntuacion"] += 1

    transferir_cartas(ganador, carta1, carta2, mazo_jugadores, datos_jugadores)
    resolver_empate(ganador, pilon_mesa, mazo_jugadores, datos_jugadores)
    incrementar_victorias_elementales(atributo_elegido, ganador, datos_jugadores)

    return ganador




def determinar_ganador_final(datos_jugadores: dict, mazo_jugadores: dict) -> None:
    cartas_j1 = len(mazo_jugadores["jugador1"])
    cartas_j2 = len(mazo_jugadores["jugador2"])

    ganador = None  


    if datos_jugadores["jugador1"]["Victorias Elementales"] >= 10:
        ganador = "jugador1"
        print(f"\n{datos_jugadores['jugador1']['nombre']} gana el juego con {datos_jugadores['jugador1']['Victorias Elementales']} victorias elementales!")
    
    elif datos_jugadores["jugador2"]["Victorias Elementales"] >= 10:
        ganador = "jugador2"
        print(f"\n{datos_jugadores['jugador2']['nombre']} gana el juego con {datos_jugadores['jugador2']['Victorias Elementales']} victorias elementales!")

    
    if ganador  == None:  
        print("\nResumen final de las cartas:")
        print(f"{datos_jugadores['jugador1']['nombre']} tiene {cartas_j1} cartas.")
        print(f"{datos_jugadores['jugador2']['nombre']} tiene {cartas_j2} cartas.")
        
        if cartas_j1 > cartas_j2:
            ganador = "jugador1"
            print(f"{datos_jugadores['jugador1']['nombre']} es el ganador final por tener más cartas.")
        elif cartas_j2 > cartas_j1:
            ganador = "jugador2"
            print(f"{datos_jugadores['jugador2']['nombre']} es el ganador final por tener más cartas.")
        else:
            print("El juego termina en empate, ambos jugadores tienen la misma cantidad de cartas.")

    return ganador 
