import pygame
from boton import *
from funciones_pygame import *

def inicializar_ventana():
    ANCHO_VENTANA = 1280
    ALTO_VENTANA = 720

    pygame.init()
    pygame.mixer.init()

    ventana_ppal = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
    
    pygame.display.set_caption("POKE CARDS")
    
    icono = pygame.image.load(r"pokemon_icono.png")
    pygame.display.set_icon(icono)

    fondo = pygame.image.load(r"pikachu.jpg")
    fondo = pygame.transform.scale(fondo,(ANCHO_VENTANA, ALTO_VENTANA))

    return ventana_ppal, fondo


def crear_botones_dinamicos(ventana_ppal):
    lista = []
    dimension = (100,100)
    paths = [r"PLAY.png",r"RANKING.png" , r"CERRAR.png"]
    posicion_inicial = [500,80]
    acciones = ["jugar" , "ranking" , "salir"]
    i = 0
    for accion in acciones:
        funcion = globals()[accion]
        boton = crear_boton(dimension,posicion_inicial,ventana_ppal,funcion,paths[i])
        lista.append(boton)
        posicion_inicial = [posicion_inicial[0], posicion_inicial[1] + 200] 
        i += 1
    return lista
