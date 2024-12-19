import pygame
from boton import *
from funciones_pygame import *

def inicializar_ventana():
    ANCHO_VENTANA = 1280
    ALTO_VENTANA = 720

    pygame.init()
    ventana_ppal = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
    
    pygame.display.set_caption("POKE CARDS")
    
    icono = pygame.image.load(r"pokemon_icono.png")
    pygame.display.set_icon(icono)

    fondo = pygame.image.load(r"fondo.jpg")
    fondo = pygame.transform.scale(fondo,(ANCHO_VENTANA, ALTO_VENTANA))

    return ventana_ppal, fondo


def crear_botones_dinamicos(ventana_ppal):
    lista = []
    dimension = (200, 60)  
    posicion_inicial = [320, 650] 
    acciones = ["jugar", "ranking", "salir"]
    textos = ["Play", "Ranking", "Close"]
    espaciado = 20 

    for i, (accion, texto) in enumerate(zip(acciones, textos)):
        funcion = globals()[accion]
        posicion = [posicion_inicial[0] + i * (dimension[0] + espaciado), posicion_inicial[1]]
        boton = crear_boton(dimension, posicion, ventana_ppal, funcion, texto)
        lista.append(boton)

    return lista