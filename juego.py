from utilities import *
from mazo import *
from jugadores import *
from funciones import *
from tateti import *





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

def jugar_ronda(ronda: int, datos_jugadores: dict, mazo_jugadores: dict, mesas: list) -> str:
    '''Printeamos la ronda actual'''
    print(f"\nRonda: {ronda}")
    '''Sacamos una carta de cada mazo'''
    carta1 = mazo_jugadores["jugador1"].pop(0)
    carta2 = mazo_jugadores["jugador2"].pop(0)
    '''Elegimos un atributo aleatorio y lo mostramos'''
    atributo_elegido = elegir_atributo_aleatorio(atributos)
    print(f"Atributo elegido: {atributo_elegido}")
    '''Llamamos a la funcion para comparar las cartas'''
    resultado_comparacion = comparar_cartas(carta1, carta2, atributo_elegido)
    '''Mostramos las cartas de cada jugador'''
    mostrar_carta(carta1, datos_jugadores["jugador1"]["nombre"])
    mostrar_carta(carta2, datos_jugadores["jugador2"]["nombre"])
    '''Determinamos el ganador y lo devolvemos'''
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
            break
        ronda += 1
    '''Cuando el juego termina, guardamos los datos de los jugadores'''
    guardar_datos_jugadores(datos_jugadores)
