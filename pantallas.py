import pygame
from input import *
from boton import *
from juego_pygame import *
from ordenamiento import *


def pantalla_inicio(ventana, fondo, lista_botones):
    ventana.blit(fondo, (0, 0))
    for boton in lista_botones:  
        dibujar(boton)
    # for i in range(3):
    #       dibujar_botones([lista_botones[i]])
    # boton_sonido = toggle_sound_button(ventana)

def pantalla_ingresar_nombres(ventana_ppal, fondo, input1, input2, jugadores,input1_pos,input2_pos):
            ventana_ppal.fill((0, 0, 0)) 

            fondo_opaco = pygame.Surface((ventana_ppal.get_width(), ventana_ppal.get_height()))
            fondo_opaco.set_alpha(128)  
            fondo_opaco.fill((0, 0, 0))
            ventana_ppal.blit(fondo, (0, 0))
            ventana_ppal.blit(fondo_opaco, (0, 0)) 

            fuente = pygame.font.SysFont("consolas", 30)
            texto_jugador1 = fuente.render(f"Jugador 1: {jugadores.get('jugador1', 'Esperando...')}", True, (255, 255, 255))
            texto_jugador2 = fuente.render(f"Jugador 2: {jugadores.get('jugador2', 'Esperando...')}", True, (255, 255, 255))

            ventana_ppal.blit(texto_jugador1, (input1_pos[0], input1_pos[1] - 40))
            ventana_ppal.blit(texto_jugador2, (input2_pos[0], input2_pos[1] - 40))

            dibujar_input(input1)
            dibujar_input(input2)
            boton_sonido = toggle_sound_button(ventana_ppal)

def pantalla_jugando(ventana, datos_jugadores, mazo_jugadores):
    jugar_con_pygame(datos_jugadores, mazo_jugadores)
    


def pantalla_ranking(ventana, fondo):

    archivo_json = "historial_partidas.json"
    historial_partidas = manejar_archivo_json(archivo_json, "leer")
    

    jugadores_del_historial = obtener_jugadores_del_historial(historial_partidas)
    jugadores_ordenados = bubble_sort(jugadores_del_historial, "puntuacion", "desc") 


    fondo = pygame.transform.scale(fondo, (ventana.get_width(), ventana.get_height()))  
    ventana.blit(fondo, (0, 0))
    boton_atras = crear_boton((150, 50), (1100, 20),ventana,texto="Atras")
    dibujar(boton_atras)
    boton_sonido = toggle_sound_button(ventana)

    mostrar_jugadores_ordenados(jugadores_ordenados, ventana)

    pygame.display.update()
   


