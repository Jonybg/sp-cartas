from utilities import *
from mazo import *
from jugadores import *
from funciones import *
from tateti import *
import time





def obtener_jugadores() -> dict:
    '''Obtenemos los nombres de los jugadores'''
    datos_jugadores = obtener_nombres_jugadores()
    return datos_jugadores

def preparar_mazo() -> dict:
    '''Cargamos el mazo, lo mezclamos y repartimos las cartas'''
    mazo = cargar_mazo("cartas.csv")
    mazo_jugadores = mezclar_mazo(mazo)
    mazo_mezclado = repartir_cartas(mazo_jugadores)
    return mazo_mezclado

def mostrar_carta(carta: dict, nombre: str) -> None:
    '''Printeamos las cartas de cada jugador'''
    print(f"\nCarta del jugador {nombre}:")
    '''Mostramos el atributo y su valor'''
    for atributo, valor in carta.items():
        print(f"{atributo}: {valor}")

def sacar_carta_de_cada_jugador(mazo_jugadores: dict):
    return ((mazo_jugadores["jugador1"].pop(0)), (mazo_jugadores["jugador2"].pop(0)))

def mostrar_carta_jugadores(carta1: dict, carta2: dict, datos_jugadores: dict) -> None:
    cartas = {"jugador1": carta1, "jugador2": carta2}
    for jugador, carta in cartas.items():
        mostrar_carta(carta, datos_jugadores[jugador]["nombre"])


def jugar_ronda(ronda: int, datos_jugadores: dict, mazo_jugadores: dict, mesas: list) -> str:
    
    print(f"\nRonda: {ronda}")
    
    carta1, carta2 = sacar_carta_de_cada_jugador(mazo_jugadores)
    
    atributo_elegido = elegir_atributo_aleatorio(atributos)
    print(f"Atributo elegido: {atributo_elegido}")
    
    resultado_comparacion = comparar_cartas(carta1, carta2, atributo_elegido)
    
    mostrar_carta_jugadores(carta1, carta2, datos_jugadores)

    ganador = ganador_ronda(resultado_comparacion, carta1, carta2, datos_jugadores, mazo_jugadores, mesas, atributo_elegido)
    return ganador



def verificar_condiciones_de_victoria(datos_jugadores: dict, mazo_jugadores: dict, ronda: int, max_rondas: int) -> str:
    '''Llamamos a todas las funciones para verificar las condiciones de victoria'''
    ganador_final = None
    ganador_por_cartas = verificar_ganador_por_cartas(mazo_jugadores)
    ganador_por_rondas = verificar_ganador_por_rondas(mazo_jugadores, ronda, max_rondas)
    ganador_por_victorias_elementales = verificar_victorias_elementales(datos_jugadores)
    '''Verificamos si alguno de los jugadores ha ganado por cartas, rondas o victorias 
       elementales y printea el ganador'''
    if ganador_por_cartas:
        print(f"{datos_jugadores[ganador_por_cartas]['nombre']} es el ganador porque se ha quedado con todas las cartas.")
        ganador_final = ganador_por_cartas
    
    elif ganador_por_rondas:
        print(f"{datos_jugadores[ganador_por_rondas]['nombre']} gana por tener más cartas tras {max_rondas} rondas.")
        ganador_final = ganador_por_rondas

    elif ganador_por_victorias_elementales:
        print(f"{datos_jugadores[ganador_por_victorias_elementales]['nombre']} gana con 10 victorias elementales.")
        ganador_final = ganador_por_victorias_elementales
    '''Si hay ganador por cartas, rondas o victorias elementales, termina el juego'''
    return ganador_final

def ejecutar_juego():
    '''Funcion principal del juego'''
    datos_jugadores = obtener_jugadores()
    mazo_jugadores = preparar_mazo()
    mesas = []
    max_rondas =250
    ronda = 1
    '''El juego se repite hasta que un jugador gane por cartas, rondas o victorias elementales'''
    while ronda <= max_rondas:
        jugar_ronda(ronda, datos_jugadores, mazo_jugadores, mesas)
        ganador_final = verificar_condiciones_de_victoria(datos_jugadores, mazo_jugadores, ronda, max_rondas)
        if ganador_final:
            guardar_datos_jugadores(datos_jugadores,ganador_final)
            break
        ronda += 1
        # time.sleep(2)
    '''Cuando el juego termina, guardamos los datos de los jugadores'''
   