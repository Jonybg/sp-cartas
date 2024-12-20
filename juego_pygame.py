import random
import pygame
from time import sleep
from mazo import *
from jugadores import *
from tateti import *
from juego import *
from input import *
from boton import *
import pygame
EVENTO_CLICK_BOTON = pygame.USEREVENT + 1
EVENTO_INPUT_SELECCIONADO = pygame.USEREVENT + 2
EVENTO_NOMBRE_GUARDADO = pygame.USEREVENT + 3
EVENTO_JUEGO_LISTO = pygame.USEREVENT + 4
EVENTO_CLICK_SONIDO = pygame.event.custom_type()

campo_batalla = pygame.image.load("campo_batalla.jpg")
campo_batalla = pygame.transform.scale(campo_batalla, (1280, 720))
sonido_activado = True
def reproducir_musica():
    pygame.mixer.music.load("intro.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
def toggle_sound():
    """Activa o desactiva el sonido globalmente (música y efectos)."""
    global sonido_activado
    if sonido_activado:
        pygame.mixer.music.set_volume(0) 
        pygame.mixer.stop()  
        sonido_activado = False
    else:
        pygame.mixer.music.set_volume(0.5)  
        sonido_activado = True
def reproducir_efecto_sonido(sonido_path):
    """Reproduce un efecto de sonido si el sonido está activado."""
    if sonido_activado:
        efecto_sonido = pygame.mixer.Sound(sonido_path)
        efecto_sonido.set_volume(0.5)  
        efecto_sonido.play()
def manejar_click_sonido(evento, boton_sonido):
    """Handles clicking the sound toggle button."""
    if evento.type == pygame.MOUSEBUTTONDOWN:
        if boton_sonido["Rectangulo"].collidepoint(evento.pos):
            toggle_sound()  
    return boton_sonido
def preparar_datos_jugadores(jugadores):
    datos_jugadores = {}
    for key, nombre in jugadores.items():
        datos_jugadores[key] = {
            "nombre": nombre, 
            "puntuacion": 0, 
            "Victorias Elementales": 0
        }
    return datos_jugadores
def crear_boton_inicio(ventana):
    boton_atras = crear_boton((100, 50), (1150, 20), ventana, texto="Inicio")
    dibujar(boton_atras)
    return boton_atras

def manejar_click_sonido(evento, boton_sonido):
    """Maneja el clic en el botón de sonido."""
    if evento.type == EVENTO_CLICK_SONIDO:
        if boton_sonido["Rectangulo"].collidepoint(evento.pos):
            toggle_sound()
    return boton_sonido
def manejar_evento_cierre(evento, flag_run):
    """Maneja el evento de cierre de la ventana."""
    if evento.type == pygame.QUIT:
        flag_run = False
    return flag_run
def manejar_click_boton(lista_botones, evento, fase):
    """Maneja los clics en los botones."""
    if fase == "ranking" and lista_botones[-1]["Rectangulo"].collidepoint(evento.pos):
        fase = "inicio"
    elif lista_botones[-2]["Rectangulo"].collidepoint(evento.pos):
        fase = "ranking"
    elif fase == "inicio" and lista_botones[0]["Rectangulo"].collidepoint(evento.pos):
        fase = "ingresar_nombres"
    elif fase == "inicio" and lista_botones[2]["Rectangulo"].collidepoint(evento.pos):
        pygame.quit()
    return fase


def manejar_click_inputs(evento, input1, input2, input_activo):
    """Maneja los clics en los inputs."""
    if input1["Rectangulo"].collidepoint(evento.pos):
        cambiar_color(input1)
        input_activo = "input1"
    elif input2["Rectangulo"].collidepoint(evento.pos):
        cambiar_color(input2)
        input_activo = "input2"
    return input_activo

def manejar_escritura(evento, input_activo, input1, input2):
    """Maneja la escritura en los inputs activos."""
    if input_activo == "input1" and input1["Activo"]:
        escribir(input1, evento)
    elif input_activo == "input2" and input2["Activo"]:
        escribir(input2, evento)

def manejar_guardado_jugadores(evento, input1, input2, jugadores):
    """Maneja el guardado de nombres de los jugadores."""
    if evento.key == pygame.K_RETURN:
        if input1["Activo"]:
            print(f"Guardando Jugador 1: {input1['Texto']}")
            jugadores["jugador1"] = input1["Texto"]
            input1["Activo"] = False
            input1["Texto"] = ""
        elif input2["Activo"]:
            print(f"Guardando Jugador 2: {input2['Texto']}")
            jugadores["jugador2"] = input2["Texto"]
            input2["Activo"] = False
            input2["Texto"] = ""
    return jugadores

def manejar_boton_atras(evento, boton_atras, fase):
    """Maneja el clic del botón de atras para salir de la fase de jugando."""
    if evento.type == pygame.MOUSEBUTTONDOWN:
        if boton_atras["Rectangulo"].collidepoint(evento.pos):
            fase= "inicio"  
    return fase
def manejar_boton_inicio(evento, boton_inicio, fase):
    if evento.type == pygame.MOUSEBUTTONDOWN:
        if boton_inicio["Rectangulo"].collidepoint(evento.pos):
            print("Botón de inicio clickeado!")
            fase = "inicio"
    return fase
def renderizar_boton_atras(pantalla, fuente):
    """Renderiza el botón de atrás en la fase de jugando."""
    boton_atras = crear_boton((150, 50), (1100, 600), pantalla, texto="Atrás")  
    dibujar(boton_atras)
    return boton_atras

def manejar_eventos_cierre(eventos):
    for evento in eventos:
        if evento.type == pygame.QUIT:
            return False
    return True
def manejar_eventos_click(lista_botones, evento, fase):
    if evento.type == pygame.MOUSEBUTTONDOWN:
        nuevo_fase = manejar_click_boton(lista_botones, evento, fase)
        return nuevo_fase
    return fase

def manejar_inputs_activos(evento, input1, input2, input_activo):
    if evento.type == pygame.MOUSEBUTTONDOWN:
        return manejar_click_inputs(evento, input1, input2, input_activo)
    return input_activo

def manejar_eventos_escritura(evento, input_activo, input1, input2, jugadores):
    if evento.type == pygame.KEYDOWN:
        manejar_escritura(evento, input_activo, input1, input2)
        jugadores_actualizados = manejar_guardado_jugadores(evento, input1, input2, jugadores)
        return jugadores_actualizados
    return jugadores
def manejar_eventos_sonido(evento, boton_sonido):
    if evento.type == pygame.MOUSEBUTTONDOWN:
        return manejar_click_sonido(evento, boton_sonido)
    return boton_sonido
def manejar_estado_fase(evento, fase, jugadores):
    if jugadores.get("jugador1") and jugadores.get("jugador2"):
        pygame.event.post(pygame.event.Event(EVENTO_JUEGO_LISTO))
        return "jugando"
    return fase
def manejador_eventos_cierre(eventos):
    for evento in eventos:
        if evento.type == pygame.QUIT:  
            return False 
    return True
def manejador_eventos(lista_botones, input1, input2, input_activo, fase, jugadores, ventana, boton_sonido):
    eventos = pygame.event.get()
    flag_run = manejar_eventos_cierre(eventos)

    for evento in eventos:
        fase = manejar_eventos_click(lista_botones, evento, fase)
        input_activo = manejar_inputs_activos(evento, input1, input2, input_activo)
        jugadores = manejar_eventos_escritura(evento, input_activo, input1, input2, jugadores)
        boton_sonido = manejar_eventos_sonido(evento, boton_sonido)
        fase = manejar_estado_fase(evento, fase, jugadores)
        if fase == "ranking":
            boton_atras = crear_boton((150, 50), (1100, 20), ventana, texto="Atrás")
            dibujar(boton_atras)  
            fase = manejar_boton_atras(evento, boton_atras, fase)
    return {
        "flag_run": flag_run,
        "input_activo": input_activo,
        "fase": fase,
        "jugadores": jugadores,
    }
def toggle_sound_button(ventana):
    """Creates and draws a toggle sound button."""
    boton_sonido = crear_boton((100, 50),(20, 20),ventana, texto="Sonido")
    dibujar(boton_sonido)
    return boton_sonido
def agregar_cartas_a_mazo(mazo: list, carta1: dict, carta2: dict) -> None:
    mazo.extend([carta1, carta2])

def cargar_plantilla_carta(pos_x, pos_y):
    try:
        plantilla = pygame.image.load("template.jpg").convert_alpha()
        plantilla = pygame.transform.scale(plantilla, (200, 300))
        return plantilla
    except :
        print("Error al cargar la plantilla de fondo: template.png")
        return None

def cargar_sprite_pokemon(carta, pos_x, pos_y):
    try:
        sprite = pygame.image.load(carta["path"]).convert_alpha()
        sprite = pygame.transform.scale(sprite, (100, 100))
        return sprite
    except :
        print(f"Error al cargar el sprite: {carta['path']}")
        return None

def cargar_icono_elemento(carta, pos_x, pos_y):
    try:
        elemento_sprite = pygame.image.load(carta["elemento_imagen"]).convert_alpha()
        elemento_sprite = pygame.transform.scale(elemento_sprite, (30, 30))
        return elemento_sprite
    except :
        print(f"Error al cargar el ícono del elemento: {carta['elemento_imagen']}")
        return None

def dibujar_propiedades_carta(pantalla, carta, pos_x, pos_y):
    propiedades = [
        (f"{carta['nombre']}", pos_x + 75, pos_y + 20),
        (f"Velocidad", pos_x + 20, pos_y + 190),
        (f"{carta['velocidad']}", pos_x + 120, pos_y + 190),
        (f"Fuerza", pos_x + 20, pos_y + 210),
        (f"{carta['fuerza']}", pos_x + 120, pos_y + 210),
        (f"Peso", pos_x + 20, pos_y + 230),
        (f"{carta['peso']:.1f}", pos_x + 120, pos_y + 230),
        (f"Altura", pos_x + 20, pos_y + 250),
        (f"{carta['altura']:.1f}", pos_x + 120, pos_y + 250),
    ]

    fuente_propiedades = pygame.font.Font(None, 18)
    for texto, x, y in propiedades:
        texto_renderizado = fuente_propiedades.render(texto, True, (0, 0, 0))
        pantalla.blit(texto_renderizado, (x, y))

def renderizar_carta(pantalla, carta, pos_x, pos_y, fuente, nombre_jugador):
    plantilla = cargar_plantilla_carta(pos_x, pos_y)
    if plantilla:
        pantalla.blit(plantilla, (pos_x, pos_y))

    sprite_pokemon = cargar_sprite_pokemon(carta, pos_x, pos_y)
    if sprite_pokemon:
        pantalla.blit(sprite_pokemon, (pos_x + 50, pos_y + 50))

    icono_elemento = cargar_icono_elemento(carta, pos_x, pos_y)
    if icono_elemento:
        pantalla.blit(icono_elemento, (pos_x + 160, pos_y + 10))

    reproducir_efecto_sonido(carta["sonido_pokemon"])
    dibujar_propiedades_carta(pantalla, carta, pos_x, pos_y)
    renderizar_texto(pantalla, nombre_jugador, pos_x + 80, pos_y - 30, fuente)

def renderizar_texto(pantalla, texto, pos_x, pos_y, fuente):
    texto_renderizado = fuente.render(texto, True, (0, 0, 0))
    pantalla.blit(texto_renderizado, (pos_x, pos_y))

def mostrar_tablero_tateti(pantalla, tablero, fuente):
    y_pos = 150
    for fila in tablero:
        fila_texto = " | ".join(fila)
        texto_renderizado = fuente.render(fila_texto, True, (0, 0, 0))
        pantalla.blit(texto_renderizado, (500, y_pos))
        y_pos += 40

def mostrar_cartas_ronda(pantalla, carta1, carta2, fuente, atributo_elegido, nombre_jugador1, nombre_jugador2):
    pantalla.blit(campo_batalla, (0, 0))  
    renderizar_carta(pantalla, carta1, 100, 200, fuente, nombre_jugador1)
    renderizar_carta(pantalla, carta2, 950, 200, fuente, nombre_jugador2)
    renderizar_texto(pantalla, f"Atributo elegido: {atributo_elegido}", 500, 50, fuente)
def mostrar_pantalla_victoria(pantalla, mensaje, fuente):
    """Función que muestra la pantalla con el mensaje de victoria."""
    
    fondo_victoria = pygame.image.load("fondo.jpg")  
    fondo_victoria = pygame.transform.scale(fondo_victoria, (1280, 720))  
    pantalla.blit(fondo_victoria, (0, 0))   
    renderizar_texto(pantalla, mensaje, 50, 300, fuente)
    pygame.display.flip()  
    sleep(2) 
    pygame.display.update()
def verificar_condiciones_de_victoria(pantalla, fuente, datos_jugadores: dict, mazo_jugadores: dict, ronda: int, max_rondas: int) -> str:
    '''Verifica las condiciones de victoria y muestra el mensaje en la pantalla final con el fondo.'''
    ganador_final = None
    ganador_por_cartas = verificar_ganador_por_cartas(mazo_jugadores)
    ganador_por_rondas = verificar_ganador_por_rondas(mazo_jugadores, ronda, max_rondas)
    ganador_por_victorias_elementales = verificar_victorias_elementales(datos_jugadores)

    mensaje = None  
    if ganador_por_cartas:
        mensaje = f"{datos_jugadores[ganador_por_cartas]['nombre']} es el ganador porque se ha quedado con todas las cartas."
        ganador_final = ganador_por_cartas
    elif ganador_por_rondas:
        mensaje = f"{datos_jugadores[ganador_por_rondas]['nombre']} gana por tener más cartas tras {max_rondas} rondas."
        ganador_final = ganador_por_rondas
    elif ganador_por_victorias_elementales:
        mensaje = f"{datos_jugadores[ganador_por_victorias_elementales]['nombre']} gana con 10 victorias elementales."
        ganador_final = ganador_por_victorias_elementales

    fondo = pygame.image.load("fondo.jpg") 
    fondo = pygame.transform.scale(fondo, (1280, 720)) 

    pantalla.blit(fondo, (0, 0))


   
        
    if mensaje:  
        mostrar_pantalla_victoria(pantalla, mensaje, fuente)

    return ganador_final

def agregar_a_mesa(pilon_mesa: list, carta1: dict, carta2: dict, pantalla, fuente) -> None:
    '''Agrega las cartas a la mesa y muestra un mensaje en pantalla'''
    mensaje = "Es un empate, ambas cartas se guardan en el pilón de mesa."
    agregar_cartas_a_mazo(pilon_mesa, carta1, carta2)
    renderizar_texto(pantalla, mensaje, 500, 100, fuente)  


def transferir_cartas(ganador: str, carta1: dict, carta2: dict, mazo_jugadores: dict, datos_jugadores: dict, pantalla, fuente) -> None:
    '''Transfiere las cartas al ganador e imprime el ganador de la ronda en la pantalla'''
    agregar_cartas_a_mazo(mazo_jugadores[ganador], carta1, carta2)
    mensaje = f"{datos_jugadores[ganador]['nombre']} gana la ronda y recibe las cartas"
    renderizar_texto(pantalla, mensaje, 500, 100, fuente)  


def mostrar_resultado_ronda(pantalla, ganador, fuente):
    mensaje = f"Ganador de la ronda: {ganador}"
    renderizar_texto(pantalla, mensaje, 500, 80, fuente) 
    # pygame.display.flip()
    sleep(0.2)
def preparar_ronda_juego(datos_jugadores, mazo_jugadores):
    carta1, carta2 = sacar_carta_de_cada_jugador(mazo_jugadores)
    atributo_elegido = elegir_atributo_aleatorio(atributos)
    return carta1, carta2, atributo_elegido

def procesar_resultado_ronda(carta1, carta2, atributo_elegido, datos_jugadores, mazo_jugadores, pilon_mesa, pantalla, fuente):
    if atributo_elegido == "elemento":
        return procesar_resultado_tateti(carta1, carta2, datos_jugadores, mazo_jugadores, pilon_mesa, pantalla, fuente)
    else:
        return procesar_resultado_comparacion(carta1, carta2, atributo_elegido, datos_jugadores, mazo_jugadores, pilon_mesa, pantalla, fuente)

def procesar_resultado_tateti(carta1, carta2, datos_jugadores, mazo_jugadores, pilon_mesa, pantalla, fuente):
    resultado_tateti = jugar_tateti(carta1, carta2, datos_jugadores)
    if resultado_tateti == "jugador1":
        ganador = "jugador1"
        datos_jugadores[ganador]["puntuacion"] += 1
        datos_jugadores[ganador]["Victorias Elementales"] += 1
    elif resultado_tateti == "jugador2":
        ganador = "jugador2"
        datos_jugadores[ganador]["puntuacion"] += 1
        datos_jugadores[ganador]["Victorias Elementales"] += 1
    else:
        ganador = "Empate"
        agregar_a_mesa(pilon_mesa, carta1, carta2, pantalla, fuente)

    elementos = [carta1["elemento"], carta2["elemento"]]
    tablero = crear_tablero(elementos, 3, 3)
    return ganador, tablero

def procesar_resultado_comparacion(carta1, carta2, atributo_elegido, datos_jugadores, mazo_jugadores, pilon_mesa, pantalla, fuente):
    resultado_comparacion = comparar_cartas(carta1, carta2, atributo_elegido)
    if resultado_comparacion == "carta1":
        ganador = "jugador1"
        datos_jugadores[ganador]["puntuacion"] += 1
        agregar_cartas_a_mazo(mazo_jugadores["jugador1"], carta1, carta2)
    elif resultado_comparacion == "carta2":
        ganador = "jugador2"
        datos_jugadores[ganador]["puntuacion"] += 1
        agregar_cartas_a_mazo(mazo_jugadores["jugador2"], carta1, carta2)
    else:
        ganador = "Empate"
        agregar_a_mesa(pilon_mesa, carta1, carta2, pantalla, fuente)

    return ganador, None


def jugar_con_pygame(datos_jugadores, mazo_jugadores):
    pygame.init()
    pantalla = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Cartas - Juego por Rondas")
    fuente = pygame.font.SysFont("Consolas", 15)
    reloj = pygame.time.Clock()
    max_rondas = 250
    running = True
    ronda = 1
    pilon_mesa = []
    boton_sonido = crear_boton((100, 50), (20, 20), pantalla, texto="Sonido")
    boton_inicio = crear_boton((150, 50), (1100, 20), pantalla, texto="Inicio")
    boton_siguiente_ronda = crear_boton((150, 50), (400, 400), pantalla, texto="Siguiente Ronda")

    pygame.display.flip()
    ganador_final = None
    while running:
        for evento in pygame.event.get():  
            if evento.type == pygame.QUIT:
                running = False
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if boton_sonido["Rectangulo"].collidepoint(evento.pos):
                    toggle_sound()
                elif boton_inicio["Rectangulo"].collidepoint(evento.pos):
                    running = False
        if mazo_jugadores["jugador1"] and mazo_jugadores["jugador2"]:
            carta1, carta2, atributo_elegido = preparar_ronda_juego(datos_jugadores, mazo_jugadores)
            mostrar_cartas_ronda(pantalla, carta1, carta2, fuente, atributo_elegido, datos_jugadores["jugador1"]["nombre"],  datos_jugadores["jugador2"]["nombre"])
            ganador, tablero = procesar_resultado_ronda(carta1, carta2, atributo_elegido, datos_jugadores, mazo_jugadores, pilon_mesa, pantalla, fuente)
            if tablero:
                mostrar_tablero_tateti(pantalla, tablero, fuente)

            if ganador != "Empate" and pilon_mesa:
                transferir_cartas(ganador, carta1, carta2, mazo_jugadores, datos_jugadores, pantalla, fuente)
                resolver_empate(ganador, pilon_mesa, mazo_jugadores)
            mostrar_resultado_ronda(pantalla, ganador, fuente)
            dibujar(boton_sonido)
            dibujar(boton_inicio)
            pygame.display.flip()

            ronda += 1
            # time.sleep(5)
            ganador_final = verificar_condiciones_de_victoria(pantalla, fuente, datos_jugadores, mazo_jugadores, ronda, max_rondas)
            if ganador_final:
                guardar_datos_jugadores(datos_jugadores, ganador_final)
                return "inicio"
    
            
        else:
            running = False

    return "inicio"
