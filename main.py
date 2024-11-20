from funciones import *
from jugadores import obtener_nombres_jugadores, guardar_datos_jugadores
from mazo import cargar_mazo, dividir_mazo
from utilities import elegir_atributo_aleatorio, comparar_cartas
import time

def jugar_partida():

    while True:
        opcion = input("1:Jugar 2:Salir: ")
        match opcion:
            case "1":
                mazo = cargar_mazo("cartas.csv")
                datos_jugadores = obtener_nombres_jugadores()
                mazo_jugadores = dividir_mazo(mazo)
                rondas = 1
                mesas = []
                max_rondas = 250
                while rondas <= max_rondas:
                    print(f"\nRonda: {rondas}")

                    carta1 = mazo_jugadores["jugador1"].pop(0)
                    carta2 = mazo_jugadores["jugador2"].pop(0)

                    atributo_elegido = elegir_atributo_aleatorio()
                    print(f"Atributo elegido: {atributo_elegido}")

                    resultado = comparar_cartas(carta1, carta2, atributo_elegido)

                    print(f"La carta del jugador {datos_jugadores['jugador1']['nombre']} es: {carta1}")
                    print(f"La carta del jugador {datos_jugadores['jugador2']['nombre']} es: {carta2}")

                    ganador_ronda(resultado, carta1, carta2, datos_jugadores, mazo_jugadores, mesas, atributo_elegido)

                    ganador_por_cartas = verificar_ganador_por_cartas(mazo_jugadores, datos_jugadores)
                    if ganador_por_cartas:
                        print(f"{datos_jugadores[ganador_por_cartas]['nombre']} es el ganador porque se ha quedado con todas las cartas.")
                        break

                    if datos_jugadores["jugador1"]["Victorias Elementales"] >= 10:
                        print(f"{datos_jugadores['jugador1']['nombre']} gana con 10 victorias elementales.")
                        break
                    elif datos_jugadores["jugador2"]["Victorias Elementales"] >= 10:
                        print(f"{datos_jugadores['jugador2']['nombre']} gana con 10 victorias elementales.")
                        break

                    rondas += 1

                determinar_ganador_final(datos_jugadores, mazo_jugadores)

                guardar_datos_jugadores(datos_jugadores)
            case "2":
                print("Saliendo....")
                break
            case _:
                print("Opción inválida")

jugar_partida()
