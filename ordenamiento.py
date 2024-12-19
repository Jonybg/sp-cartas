import pygame
import json
from datetime import datetime


def manejar_archivo_json(archivo, accion):
    try:
        with open(archivo, "r") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return []


def obtener_jugadores_del_historial(historial_partidas):
    jugadores = []
    for partida in historial_partidas:
        ganador = partida["Ganador"]
        jugadores.append({
            "Fecha Partida": ganador["Fecha De partida"],
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

def mostrar_jugadores_ordenados(jugadores_ordenados, ventana):
    fuente = pygame.font.SysFont("Arial", 24)
    y_pos = 50  

    contador = 0 
    for jugador in jugadores_ordenados:
        if contador >= 5:
            break
        
        texto_fecha = fuente.render(f"Fecha de partida: {jugador['Fecha Partida']}", True, (255, 255, 255))
        texto_nombre = fuente.render(f"Nombre: {jugador['nombre']}", True, (255, 255, 255))
        texto_puntuacion = fuente.render(f"Puntuacion: {jugador['puntuacion']}", True, (255, 255, 255))
        texto_victorias = fuente.render(f"Victorias Elementales: {jugador['Victorias Elementales']}", True, (255, 255, 255))

        ventana.blit(texto_fecha, (50, y_pos +20))
        ventana.blit(texto_nombre, (50, y_pos + 50))
        ventana.blit(texto_puntuacion, (50, y_pos + 80))
        ventana.blit(texto_victorias, (50, y_pos + 110))

        y_pos += 130  
        contador += 1  


def pantalla_ranking(ventana,fondo):
   
    archivo_json = "historial_partidas.json"
    historial_partidas = manejar_archivo_json(archivo_json, "leer")
    

    jugadores_del_historial = obtener_jugadores_del_historial(historial_partidas)
    jugadores_ordenados = bubble_sort(jugadores_del_historial, "puntuacion", "desc")  

   
    ventana.blit(fondo, (0, 0))
    mostrar_jugadores_ordenados(jugadores_ordenados, ventana)

    pygame.display.update() 

# from datetime import datetime
# from jugadores import *

# def obtener_jugadores_del_historial(historial_partidas):

#     jugadores = []
#     for partida in historial_partidas:
#         ganador = partida["Ganador"]
#         jugadores.append({
#             "Fecha Partida": ganador["Fecha De partida"],
#             "nombre": ganador["Nombre"],
#             "puntuacion": ganador["Puntuacion"],
#             "Victorias Elementales": ganador["Victorias Elementales"]
#         })
#     return jugadores

# def bubble_sort(jugadores, criterio, orden):

#     for i in range(len(jugadores) - 1):
#         for j in range(i + 1, len(jugadores)):
#             valor_1 = jugadores[i][criterio]
#             valor_2 = jugadores[j][criterio]

#             if orden == "asc" and valor_1 > valor_2:
#                 jugadores[i], jugadores[j] = jugadores[j], jugadores[i]
#             elif orden == "desc" and valor_1 < valor_2:
#                 jugadores[i], jugadores[j] = jugadores[j], jugadores[i]

#     return jugadores

# def mostrar_jugadores_ordenados(jugadores_ordenados):
#     print("\nJugadores ordenados:")
#     contador = 0 
#     for jugador in jugadores_ordenados:
#         print(f"Fecha de partida: {jugador['Fecha Partida']}")
#         print(f"Nombre: {jugador['nombre']}")
#         print(f"Puntuacion: {jugador['puntuacion']}")
#         print(f"Victorias Elementales: {jugador['Victorias Elementales']}\n")
#         contador += 1
#         if contador >= 5:
#             break 

# def ordenar(criterio, orden):

#     archivo_json = "historial_partidas.json"
#     historial_partidas = manejar_archivo_json(archivo_json, "leer") 
#     jugadores_del_historial = obtener_jugadores_del_historial(historial_partidas)
#     jugadores_ordenados = bubble_sort(jugadores_del_historial, criterio, orden)
#     mostrar_jugadores_ordenados(jugadores_ordenados)