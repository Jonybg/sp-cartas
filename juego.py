from utilities import *
from mazo import *
from jugadores import *
from funciones import *

def iniciar_partida():
    mazo = cargar_mazo("cartas.csv")
    datos_jugadores = obtener_nombres_jugadores()
    mazo_jugadores = dividir_mazo(mazo)
    return datos_jugadores, mazo_jugadores

def jugar_ronda(ronda, datos_jugadores, mazo_jugadores, mesas):
    print(f"\nRonda: {ronda}")

    carta1 = mazo_jugadores["jugador1"].pop(0)
    carta2 = mazo_jugadores["jugador2"].pop(0)

    atributo_elegido = elegir_atributo_aleatorio()
    print(f"Atributo elegido: {atributo_elegido}")

    resultado = comparar_cartas(carta1, carta2, atributo_elegido)

    print(f"La carta del jugador {datos_jugadores['jugador1']['nombre']} es: {carta1}")
    print(f"La carta del jugador {datos_jugadores['jugador2']['nombre']} es: {carta2}")

    ganador_ronda(resultado, carta1, carta2, datos_jugadores, mazo_jugadores, mesas, atributo_elegido)

def verificar_condiciones_de_victoria(datos_jugadores, mazo_jugadores):
    ganador_por_cartas = verificar_ganador_por_cartas(mazo_jugadores, datos_jugadores)
    if ganador_por_cartas:
        print(f"{datos_jugadores[ganador_por_cartas]['nombre']} es el ganador porque se ha quedado con todas las cartas.")
        return ganador_por_cartas

    if datos_jugadores["jugador1"]["Victorias Elementales"] >= 10:
        print(f"{datos_jugadores['jugador1']['nombre']} gana con 10 victorias elementales.")
        return "jugador1"

    if datos_jugadores["jugador2"]["Victorias Elementales"] >= 10:
        print(f"{datos_jugadores['jugador2']['nombre']} gana con 10 victorias elementales.")
        return "jugador2"

    return None

def ejecutar_juego():
    datos_jugadores, mazo_jugadores = iniciar_partida()
    mesas = []
    max_rondas = 250
    ronda = 1

    while ronda <= max_rondas:
        jugar_ronda(ronda, datos_jugadores, mazo_jugadores, mesas)
        ganador = verificar_condiciones_de_victoria(datos_jugadores, mazo_jugadores)
        if ganador:
            break
        ronda += 1 

    determinar_ganador_final(datos_jugadores, mazo_jugadores)
    guardar_datos_jugadores(datos_jugadores)

