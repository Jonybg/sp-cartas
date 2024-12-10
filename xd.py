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

def agregar_cartas_a_mazo(mazo: list, carta1: dict, carta2: dict) -> None:
    mazo.extend([carta1, carta2])

def renderizar_carta(pantalla, carta, pos_x, pos_y, fuente, nombre_jugador):
    try:
        plantilla = pygame.image.load("template.jpg").convert_alpha()
        plantilla = pygame.transform.scale(plantilla, (200, 300))
        pantalla.blit(plantilla, (pos_x, pos_y))
    except pygame.error:
        print("Error al cargar la plantilla de fondo: template.jpg")

    try:
        sprite = pygame.image.load(carta["path"]).convert_alpha()
        sprite = pygame.transform.scale(sprite, (100, 100))
        pantalla.blit(sprite, (pos_x + 50, pos_y + 40))
    except pygame.error:
        print(f"Error al cargar el sprite: {carta['path']}")

    # Renderizar el nombre de la carta en la parte superior central
    texto_nombre_carta = fuente.render(carta["nombre"], True, (0, 0, 0))  # Cambia "nombre" por la clave adecuada
    pantalla.blit(texto_nombre_carta, (pos_x + 80, pos_y + 20))  # Posición fija

    # Renderizar propiedades de la carta
    propiedades = [
        ("Velocidad:", round(carta["velocidad"]), pos_x + 20, pos_y + 190),  # Redondea y elimina decimales
        ("Fuerza:", round(carta["fuerza"]), pos_x + 20, pos_y + 210),        # Redondea y elimina decimales
        ("Peso:", round(carta["peso"]), pos_x + 20, pos_y + 230),           # Redondea y elimina decimales
        ("Altura:", round(carta["altura"]), pos_x + 20, pos_y + 250),       # Redondea y elimina decimales
    ]

    for descripcion, valor, x, y in propiedades:
        texto_descripcion = fuente.render(descripcion, True, (0, 0, 0))
        texto_valor = fuente.render(str(valor), True, (0, 0, 0))

        # Renderiza la descripción
        pantalla.blit(texto_descripcion, (x, y))
        
        # Renderiza el valor con un desplazamiento
        pantalla.blit(texto_valor, (x + 140, y))

    # Renderizar el nombre del jugador (ya implementado)
    renderizar_texto(pantalla, nombre_jugador, pos_x + 10, pos_y + 280, fuente)



def renderizar_texto(pantalla, texto, pos_x, pos_y, fuente):
    texto_renderizado = fuente.render(texto, True, (0, 0, 0))  
    pantalla.blit(texto_renderizado, (pos_x, pos_y))

def mostrar_tablero_tateti(pantalla, tablero, fuente):
    y_pos = 300
    x_pos = 570
    for fila in tablero:
        fila_texto = " | ".join(fila)
        texto_renderizado = fuente.render(fila_texto, True, (0, 0, 0))
        pantalla.blit(texto_renderizado, (x_pos, y_pos))
        y_pos += 40


def mostrar_cartas_ronda(pantalla, carta1, carta2, fuente, atributo_elegido, nombre_jugador1, nombre_jugador2):
    campo_batalla = pygame.image.load("fondo.jpg").convert()
    campo_batalla = pygame.transform.scale(campo_batalla, (1280, 720))
    pantalla.blit(campo_batalla, (0, 0))
    
    renderizar_carta(pantalla, carta1, 100, 200, fuente, nombre_jugador1)
    renderizar_carta(pantalla, carta2, 950, 200, fuente, nombre_jugador2)
    
    renderizar_texto(pantalla, f"Atributo elegido: {atributo_elegido}", 540, 50, fuente)
    renderizar_texto(pantalla, "Ganador de la ronda:", 540, 90, fuente)
    
    pygame.display.flip()

def verificar_condiciones_de_victoria(pantalla, fuente, datos_jugadores: dict, mazo_jugadores: dict, ronda: int, max_rondas: int) -> str:
    '''Llamamos a todas las funciones para verificar las condiciones de victoria'''
    ganador_final = None
    ganador_por_cartas = verificar_ganador_por_cartas(mazo_jugadores)
    ganador_por_rondas = verificar_ganador_por_rondas(mazo_jugadores, ronda, max_rondas)
    ganador_por_victorias_elementales = verificar_victorias_elementales(datos_jugadores)

    mensaje = None  # Variable para almacenar el mensaje a renderizar
    '''Verificamos si alguno de los jugadores ha ganado por cartas, rondas o victorias 
       elementales y renderiza el mensaje'''
    if ganador_por_cartas:
        mensaje = f"{datos_jugadores[ganador_por_cartas]['nombre']} es el ganador porque se ha quedado con todas las cartas."
        ganador_final = ganador_por_cartas
    elif ganador_por_rondas:
        mensaje = f"{datos_jugadores[ganador_por_rondas]['nombre']} gana por tener más cartas tras {max_rondas} rondas."
        ganador_final = ganador_por_rondas
    elif ganador_por_victorias_elementales:
        mensaje = f"{datos_jugadores[ganador_por_victorias_elementales]['nombre']} gana con 10 victorias elementales."
        ganador_final = ganador_por_victorias_elementales

    # Renderiza el mensaje en pantalla
    if mensaje:
        pantalla.fill((255, 255, 255))  # Limpia la pantalla con un color de fondo
        renderizar_texto(pantalla, mensaje, 50, 300, fuente)  # Cambia las coordenadas según lo necesites
        pygame.display.flip()
        sleep(2)  # Pausa para que el jugador pueda leer el mensaje

    return ganador_final

def mostrar_pantalla_final(pantalla, fuente, mensaje):
    pantalla.fill((255, 255, 255))  # Limpia la pantalla con un color de fondo
    renderizar_texto(pantalla, mensaje, 50, 300, fuente)  # Cambia las coordenadas según lo necesites
    pygame.display.flip()

    # Bucle para mantener la pantalla abierta hasta que el usuario cierre la ventana
    running = True
    while running:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                running = False

def agregar_a_mesa(pilon_mesa: list, carta1: dict, carta2: dict) -> None:
    '''Agrega las cartas a la mesa'''
    print("Es un empate, ambas cartas se guardan en el pilón de mesa.")
    agregar_cartas_a_mazo(pilon_mesa, carta1, carta2)

def transferir_cartas(ganador: str, carta1: dict, carta2: dict, mazo_jugadores: dict, datos_jugadores: dict) -> None:
    '''Transfiere las cartas al ganador e imprime el ganador de la ronda'''
    agregar_cartas_a_mazo(mazo_jugadores[ganador], carta1, carta2)
    print(f"{datos_jugadores[ganador]['nombre']} gana la ronda y recibe las cartas")
    
def mostrar_resultado_ronda(pantalla, ganador, fuente):
    texto = f"Ganador de la ronda: {ganador}"
    texto_renderizado = fuente.render(texto, True, (255, 0, 0))
    pantalla.blit(texto_renderizado, (540, 120))
    pygame.display.flip()
    sleep(0.2)
    

def jugar_con_pygame(datos_jugadores, mazo_jugadores):
    pygame.init()
    pantalla = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Cartas - Juego por Rondas")
    fuente = pygame.font.SysFont("Consolas", 10)
    reloj = pygame.time.Clock()
    max_rondas = 250
    running = True
    ronda = 1
    mesas = []

    ganador_final = None
    while running:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                running = False
        
        if mazo_jugadores["jugador1"] and mazo_jugadores["jugador2"]:
            carta1, carta2 = sacar_carta_de_cada_jugador(mazo_jugadores)
            atributo_elegido = elegir_atributo_aleatorio(atributos)

            mostrar_cartas_ronda(pantalla, carta1, carta2, fuente, atributo_elegido, datos_jugadores["jugador1"]["nombre"], datos_jugadores["jugador2"]["nombre"])

            # Aquí reutilizamos la lógica de Tateti
            if atributo_elegido == "elemento":
                resultado_tateti = jugar_tateti(carta1, carta2, datos_jugadores)
                if resultado_tateti == "jugador1":
                    ganador = datos_jugadores["jugador1"]["nombre"]
                elif resultado_tateti == "jugador2":
                    ganador = datos_jugadores["jugador2"]["nombre"]
                else:
                    ganador = "Empate"
                
                # Mostrar el tablero de Tateti en Pygame
                elementos = [carta1["elemento"], carta2["elemento"]]
                tablero = crear_tablero(elementos, 3, 3)
                mostrar_tablero_tateti(pantalla, tablero, fuente)

            else:
                # Aquí reutilizamos la lógica de comparación de cartas
                resultado_comparacion = comparar_cartas(carta1, carta2, atributo_elegido)
                if resultado_comparacion == "carta1":
                    ganador = datos_jugadores["jugador1"]["nombre"]
                    agregar_cartas_a_mazo(mazo_jugadores["jugador1"], carta1, carta2)
                elif resultado_comparacion == "carta2":
                    ganador = datos_jugadores["jugador2"]["nombre"]
                    agregar_cartas_a_mazo(mazo_jugadores["jugador2"], carta1, carta2)
                else:
                    ganador = "Ninguno (Empate)"

            # Mostrar el resultado de la ronda
            mostrar_resultado_ronda(pantalla, ganador, fuente)
            ronda += 1
            ganador_final = verificar_condiciones_de_victoria(pantalla, fuente, datos_jugadores, mazo_jugadores, ronda, max_rondas)
            if ganador_final:
                guardar_datos_jugadores(datos_jugadores, ganador_final)
                break
            ronda += 1
        else:
            running = False

    if ganador_final:
        mensaje_final = f"¡El ganador es {datos_jugadores[ganador_final]['nombre']}!"
        mostrar_pantalla_final(pantalla, fuente, mensaje_final)

    pygame.quit()
# Supón que estas funciones devuelven los datos necesarios para comenzar el juego.
datos_jugadores = obtener_jugadores()  # Devuelve los datos de los jugadores
mazo_jugadores = preparar_mazo()  # Prepara los mazos de los jugadores
jugar_con_pygame(datos_jugadores, mazo_jugadores)
