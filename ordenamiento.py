import json
from datetime import datetime

def leer_historial_partidas():
    archivo_json = "historial_partidas.json"
    try:
        with open(archivo_json, "r") as archivo:
            historial_partidas = json.load(archivo)
            return historial_partidas
    except :
        return []


def obtener_jugadores_del_historial(historial_partidas):
    jugadores = []
    for partida in historial_partidas:
        ganador = partida["Ganador"]
        jugadores.append({
            "Fecha Partida":ganador["Fecha De partida"],
            "nombre": ganador["Nombre"],
            "puntuacion": ganador["Puntuacion"],
            "Victorias Elementales": ganador["Victorias Elementales"]
    
        })
    return jugadores


def bubble_sort(jugadores, criterio, orden):
    for i in range(len(jugadores) - 1):
        for j in range(i + 1, len(jugadores)):
            valor_1 = jugadores[i][criterio]
            valor_2 = jugadores[j][criterio]

            if orden == "asc" and valor_1 > valor_2:
                jugadores[i], jugadores[j] = jugadores[j], jugadores[i]
            elif orden == "desc" and valor_1 < valor_2:
                jugadores[i], jugadores[j] = jugadores[j], jugadores[i]

    return jugadores


def mostrar_jugadores_ordenados(jugadores_ordenados):
    """Muestra la lista de jugadores ordenados con sus atributos"""
    print("\nJugadores ordenados:")
    for jugador in jugadores_ordenados:
        print(f"Fecha de partida: {jugador['Fecha Partida']}")
        print(f"\nNombre: {jugador['nombre']}")
        print(f"Puntuacion: {jugador['puntuacion']}")
        print(f"Victorias Elementales: {jugador['Victorias Elementales']}")


def ordenar(criterio, orden):
    historial_partidas = leer_historial_partidas()
    jugadores_del_historial = obtener_jugadores_del_historial(historial_partidas)
    jugadores_ordenados = bubble_sort(jugadores_del_historial, criterio, orden)
    mostrar_jugadores_ordenados(jugadores_ordenados)



