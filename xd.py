import random
import pygame
from time import sleep
from mazo import *
from jugadores import *
from tateti import *
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
    # Cargar la plantilla de fondo
    try:
        plantilla = pygame.image.load("template.jpg").convert_alpha()  # Cargar con soporte para transparencia
        plantilla = pygame.transform.scale(plantilla, (200, 300))  # Escalar al tamaño deseado
        pantalla.blit(plantilla, (pos_x, pos_y))  # Dibujar la plantilla en la posición especificada
    except pygame.error:
        print("Error al cargar la plantilla de fondo: template.png")

    # Cargar el sprite principal desde el path de la carta
    try:
        sprite = pygame.image.load(carta["path"]).convert_alpha() # Usar transparencia si es necesario
        sprite = pygame.transform.scale(sprite, (100, 100))  # Redimensionar la imagen
        pantalla.blit(sprite, (pos_x + 50, pos_y + 40))  # Dibujar la imagen en la carta
    except pygame.error:
        print(f"Error al cargar el sprite: {carta['path']}")

    # Renderizar la imagen del elemento
    try:
        elemento_sprite = pygame.image.load(carta["elemento_imagen"]).convert_alpha()  # Usar transparencia
        elemento_sprite = pygame.transform.scale(elemento_sprite, (50, 50))  # Redimensionar el ícono del elemento
        pantalla.blit(elemento_sprite, (pos_x + 150, pos_y + 10))  # Posición del ícono
    except pygame.error:
        print(f"Error al cargar el ícono del elemento: {carta['elemento_imagen']}")

    # Dibujar las propiedades encima de la plantilla
    propiedades = [
        (f"{carta['nombre']}", pos_x + 75, pos_y + 20),
        (f"Velocidad: {carta['velocidad']}", pos_x + 10, pos_y + 180),
        (f"Fuerza: {carta['fuerza']}", pos_x + 10, pos_y + 200),
        (f"Elemento: {carta['elemento']}", pos_x + 10, pos_y + 220),
        (f"Peso: {carta['peso']:.1f}", pos_x + 10, pos_y + 240),
        (f"Altura: {carta['altura']:.1f}", pos_x + 10, pos_y + 260),
    ]

    # Reducir el tamaño del texto para evitar que sobresalga
    fuente_propiedades = pygame.font.Font(None, 18)  # Tamaño de fuente más pequeño
    for texto, x, y in propiedades:
        texto_renderizado = fuente_propiedades.render(texto, True, (0, 0, 0))
        pantalla.blit(texto_renderizado, (x, y))

    # Dibujar el nombre del jugador encima de la plantilla
    renderizar_texto(pantalla, nombre_jugador, pos_x + 10, pos_y + 10, fuente)


def renderizar_texto(pantalla, texto, pos_x, pos_y, fuente):
    texto_renderizado = fuente.render(texto, True, (0, 0, 0))  
    pantalla.blit(texto_renderizado, (pos_x, pos_y))


def mostrar_tablero_tateti(pantalla, tablero, fuente):
    # Centrar el tablero de Tateti en la pantalla
    y_pos = 250  # Ajustamos para centrar el tablero
    for fila in tablero:
        x_pos = 440  # Centrado horizontalmente
        for celda in fila:
            if celda.endswith(".png"):  # Asumimos que las celdas contienen paths de imágenes
                try:
                    elemento_sprite = pygame.image.load(celda)
                    elemento_sprite = pygame.transform.scale(elemento_sprite, (40, 40))
                    pantalla.blit(elemento_sprite, (x_pos, y_pos))
                except pygame.error:
                    print(f"Error al cargar el ícono del tateti: {celda}")
            else:
                texto_renderizado = fuente.render(celda, True, (0, 0, 0))
                pantalla.blit(texto_renderizado, (x_pos, y_pos))
            x_pos += 60
        y_pos += 60
    pygame.display.flip()

def mostrar_cartas_ronda(pantalla, carta1, carta2, fuente, atributo_elegido, nombre_jugador1, nombre_jugador2):
    pantalla.fill((34, 139, 34))  # Color de fondo verde para el tablero
    
    # Primera carta a la izquierda y segunda carta a la derecha
    renderizar_carta(pantalla, carta1, 100, 150, fuente, nombre_jugador1)  
    renderizar_carta(pantalla, carta2, 500, 150, fuente, nombre_jugador2)  
    
    # Atributo elegido centrado en la parte superior
    renderizar_texto(pantalla, f"Atributo elegido: {atributo_elegido}", 540, 50, fuente)

    # Resultado de la ronda debajo del atributo
    renderizar_texto(pantalla, "Ganador de la ronda:", 540, 90, fuente)  
    pygame.display.flip()

def mostrar_resultado_ronda(pantalla, ganador, fuente):
    texto = f"Ganador de la ronda: {ganador}"
    texto_renderizado = fuente.render(texto, True, (255, 0, 0))
    pantalla.blit(texto_renderizado, (540, 120))  # Mostrar el resultado en una posición clara
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
                
                elementos = [carta1["elemento_imagen"], carta2["elemento_imagen"]]
                tablero = [[elementos[0]] * 3, [elementos[1]] * 3, [""] * 3]  # Tablero ejemplo
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
        sleep(10)

    pygame.quit()

# Suponiendo que estas funciones devuelven los datos necesarios para comenzar el juego.
datos_jugadores = obtener_jugadores()
mazo_jugadores = preparar_mazo()
jugar_con_pygame(datos_jugadores, mazo_jugadores)
