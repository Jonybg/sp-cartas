from utilities import *
from mazo import *
from jugadores import *
from funciones import *
from tateti import *





def obtener_jugadores():
    datos_jugadores = obtener_nombres_jugadores()
    return datos_jugadores

def preparar_mazo():
    mazo = cargar_mazo("cartas.csv")
    mazo_jugadores = mezclar_mazo(mazo)
    mazo_mezclado = repartir_cartas(mazo_jugadores)
    return mazo_mezclado

def mostrar_carta(carta, nombre):
    print(f"\nCarta del jugador {nombre}:")
    for atributo, valor in carta.items():
        print(f"{atributo}: {valor}")

def jugar_ronda(ronda, datos_jugadores, mazo_jugadores, mesas):
    print(f"\nRonda: {ronda}")

    carta1 = mazo_jugadores["jugador1"].pop(0)
    carta2 = mazo_jugadores["jugador2"].pop(0)

    atributo_elegido = elegir_atributo_aleatorio()
    print(f"Atributo elegido: {atributo_elegido}")

    resultado_comparacion = comparar_cartas(carta1, carta2, atributo_elegido)

    mostrar_carta(carta1, datos_jugadores["jugador1"]["nombre"])
    mostrar_carta(carta2, datos_jugadores["jugador2"]["nombre"])

    ganador = ganador_ronda(resultado_comparacion, carta1, carta2, datos_jugadores, mazo_jugadores, mesas, atributo_elegido)
    return ganador

def verificar_condiciones_de_victoria(datos_jugadores, mazo_jugadores,ronda,max_rondas):
    ganador = None
    ganador_por_cartas = verificar_ganador_por_cartas(mazo_jugadores, datos_jugadores)
    ganador_por_rondas = verificar_ganador_por_rondas(mazo_jugadores, ronda, max_rondas)
    if ganador_por_cartas:
        print(f"{datos_jugadores[ganador_por_cartas]['nombre']} es el ganador porque se ha quedado con todas las cartas.")
        ganador=  ganador_por_cartas
    
    elif ganador_por_rondas:
        print(f"{datos_jugadores[ganador_por_rondas]['nombre']} gana por tener más cartas tras {max_rondas} rondas.")
        ganador= ganador_por_rondas

    if datos_jugadores["jugador1"]["Victorias Elementales"] >= 10:
        print(f"{datos_jugadores['jugador1']['nombre']} gana con 10 victorias elementales.")
        ganador="jugador1"

    if datos_jugadores["jugador2"]["Victorias Elementales"] >= 10:
        print(f"{datos_jugadores['jugador2']['nombre']} gana con 10 victorias elementales.")
        ganador="jugador2"

    return ganador




def ejecutar_juego():
    datos_jugadores = obtener_jugadores()
    mazo_jugadores = preparar_mazo()
    mesas = []
    max_rondas =250
    ronda = 1

    while ronda <= max_rondas:
        jugar_ronda(ronda, datos_jugadores, mazo_jugadores, mesas)
        ganador_final = verificar_condiciones_de_victoria(datos_jugadores, mazo_jugadores, ronda, max_rondas)
        if ganador_final:
            break
        ronda += 1

    guardar_datos_jugadores(datos_jugadores)
