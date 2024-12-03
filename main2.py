import pygame
from boton import *
from funciones import *
from configuraciones import *

def manejador_eventos(lista_botones):
    flag_run = True
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            flag_run = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            checkear_accion_botones(lista_botones, evento)

    return flag_run

def main_reproductor():

    ventana_ppal, fondo = inicializar_ventana()

    #ista = crear_botones(ventana_ppal)
    # lista = crear_botones_dinamicos(ventana_ppal)
    lista = crear_botones_dinamicos_json(ventana_ppal)

    cargar_musica("Sonidos\musica.mp3")

    flag_run = True

    while flag_run:
        flag_run = manejador_eventos(lista)

        ventana_ppal.blit(fondo,(0,0))
        dibujar_botones(lista)

        pygame.display.update()

    pygame.quit()

main_reproductor()