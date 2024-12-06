import random
import pygame
from time import sleep
from mazo import *
from jugadores import *
from tateti import jugar_tateti
from juego import *
atributos = ["velocidad", "fuerza", "elemento", "peso", "altura"]

def elegir_atributo_aleatorio(atributos: list) -> str:
    return random.choice(atributos)

def comparar_cartas(carta1: dict, carta2: dict, atributo: str) -> str:
    retorno = "Empate"
    if carta1[atributo] > carta2[atributo]:
        retorno = "carta1"
    elif carta2[atributo] > carta1[atributo]:
        retorno = "carta2"
    return retorno

def agregar_cartas_a_mazo(mazo: list, carta1: dict, carta2: dict) -> None:
    mazo.extend([carta1, carta2])

def renderizar_carta(pantalla, carta, pos_x, pos_y, fuente, nombre_jugador):
    # Dibujar el contenedor de la carta
    pygame.draw.rect(pantalla, (255, 255, 255), (pos_x, pos_y, 200, 300))
    pygame.draw.rect(pantalla, (0, 0, 0), (pos_x, pos_y, 200, 300), 2)

    # Cargar el sprite desde el path de la carta
    try:
        sprite = pygame.image.load(carta["path"])
        sprite = pygame.transform.scale(sprite, (180, 100))  # Redimensionar la imagen
        pantalla.blit(sprite, (pos_x + 10, pos_y + 10))  # Dibujar la imagen en la carta
    except pygame.error:
        print(f"Error al cargar el sprite: {carta['path']}")

    # Dibujar las propiedades debajo de la imagen
    propiedades = [
        (f"Nombre: {carta['nombre']}", pos_x + 10, pos_y + 120),
        (f"Velocidad: {carta['velocidad']}", pos_x + 10, pos_y + 160),
        (f"Fuerza: {carta['fuerza']}", pos_x + 10, pos_y + 200),
        (f"Elemento: {carta['elemento']}", pos_x + 10, pos_y + 240),
        (f"Peso: {carta['peso']:.1f}", pos_x + 10, pos_y + 280),
        (f"Altura: {carta['altura']:.1f}", pos_x + 10, pos_y + 320),
    ]

    for texto, x, y in propiedades:
        texto_renderizado = fuente.render(texto, True, (0, 0, 0))
        pantalla.blit(texto_renderizado, (x, y))

    renderizar_texto(pantalla, nombre_jugador, pos_x + 10, pos_y - 30, fuente)

def renderizar_texto(pantalla, texto, pos_x, pos_y, fuente):
    texto_renderizado = fuente.render(texto, True, (0, 0, 0))  
    pantalla.blit(texto_renderizado, (pos_x, pos_y))

def mostrar_tablero_tateti(pantalla, tablero, fuente):
    y_pos = 100
    for fila in tablero:
        fila_texto = " | ".join(fila)
        texto_renderizado = fuente.render(fila_texto, True, (0, 0, 0))
        pantalla.blit(texto_renderizado, (200, y_pos))
        y_pos += 40

def mostrar_cartas_ronda(pantalla, carta1, carta2, fuente, atributo_elegido, nombre_jugador1, nombre_jugador2):
    pantalla.fill((34, 139, 34))  
    renderizar_carta(pantalla, carta1, 100, 200, fuente, nombre_jugador1)  
    renderizar_carta(pantalla, carta2, 400, 200, fuente, nombre_jugador2)  
    renderizar_texto(pantalla, f"Atributo elegido: {atributo_elegido}", 250, 50, fuente)
    pygame.display.flip()

def mostrar_resultado_ronda(pantalla, ganador, fuente):
    texto = f"Ganador de la ronda: {ganador}"
    texto_renderizado = fuente.render(texto, True, (255, 0, 0))
    pantalla.blit(texto_renderizado, (250, 100))  
    pygame.display.flip()
    sleep(0.2)  

def jugar_con_pygame(datos_jugadores, mazo_jugadores):
    pygame.init()
    pantalla = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Cartas - Juego por Rondas")
    fuente = pygame.font.Font(None, 30)
    reloj = pygame.time.Clock()

    running = True
    ronda = 1

    while running:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                running = False
        if mazo_jugadores["jugador1"] and mazo_jugadores["jugador2"]:
            carta1 = mazo_jugadores["jugador1"].pop(0)
            carta2 = mazo_jugadores["jugador2"].pop(0)
            atributo_elegido = elegir_atributo_aleatorio(atributos)

            mostrar_cartas_ronda(pantalla, carta1, carta2, fuente, atributo_elegido, datos_jugadores["jugador1"]["nombre"], datos_jugadores["jugador2"]["nombre"])

            if atributo_elegido == "elemento":
                resultado_tateti = jugar_tateti(carta1, carta2, datos_jugadores)
                if resultado_tateti == "jugador1":
                    ganador = datos_jugadores["jugador1"]["nombre"]
                elif resultado_tateti == "jugador2":
                    ganador = datos_jugadores["jugador2"]["nombre"]
                else:
                    ganador = "Empate"
                
                elementos = [carta1["elemento"], carta2["elemento"]]
                tablero = crear_tablero(elementos, 3, 3)
                mostrar_tablero_tateti(pantalla, tablero, fuente)

            else:
                resultado_comparacion = comparar_cartas(carta1, carta2, atributo_elegido)
                if resultado_comparacion == "carta1":
                    ganador = datos_jugadores["jugador1"]["nombre"]
                    agregar_cartas_a_mazo(mazo_jugadores["jugador1"], carta1, carta2)
                elif resultado_comparacion == "carta2":
                    ganador = datos_jugadores["jugador2"]["nombre"]
                    agregar_cartas_a_mazo(mazo_jugadores["jugador2"], carta1, carta2)
                else:
                    ganador = "Ninguno (Empate)"

            mostrar_resultado_ronda(pantalla, ganador, fuente)
            ronda += 1
        else:
            running = False

        reloj.tick(30)
        time.sleep(10)

    pygame.quit()

datos_jugadores = obtener_jugadores()
mazo_jugadores = preparar_mazo()
jugar_con_pygame(datos_jugadores, mazo_jugadores)
