import json
from datetime import datetime


fecha = datetime.now()
fecha_completa = fecha.strftime("%d/%m/%Y, %H:%M:%S")


def validar_nombres(nombre_jugador):
    nombre = input(f"Ingrese el nombre del jugador {nombre_jugador}: ")
    while len(nombre.strip()) == 0:
        nombre = input(
            f"El campo esta vacio.Ingrese el nombre del jugador {nombre_jugador}: ").strip()
    return nombre


def obtener_nombres_jugadores():
    datos_jugadores = {}
    for nombres_jugadores in range(1, 3):
        nombre = validar_nombres(nombres_jugadores)
        datos_jugadores[f"jugador{nombres_jugadores}"] = {
            "nombre": nombre, "puntuacion": 0, "Victorias Elementales": 0}
    return datos_jugadores


def guardar_datos_jugadores(datos_jugadores):
    archivo_json = "datos_jugadores.json"
    datos_partida = {
        "Fecha De partida": fecha_completa,
        "Jugadores": datos_jugadores

    }



    with open(archivo_json, "w") as archivo:
        json.dump(datos_partida, archivo, indent=4)
