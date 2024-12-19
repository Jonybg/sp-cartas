import pygame

def crear_boton(dimensiones, posicion, ventana, accion=None, texto=None):
    boton = {}
    boton["Ventana"] = ventana
    boton["Dimensiones"] = dimensiones
    boton["Posicion"] = posicion
    boton["Presionado"] = False
    boton["Accion"] = accion

    if texto is not None:
        font = pygame.font.SysFont('Arial', 32) 
        text_surface = font.render(texto, True, (0, 0, 0))  
        text_rect = text_surface.get_rect(center=(dimensiones[0] // 2, dimensiones[1] // 2))


        boton["Contenido"] = pygame.Surface(dimensiones)
        boton["Contenido"].fill((204, 204, 204))  

        pygame.draw.rect(boton["Contenido"], (0, 0, 0), (0, 0, dimensiones[0], dimensiones[1]), 4)

        
        boton["Contenido"].blit(text_surface, text_rect)

    boton["Rectangulo"] = boton["Contenido"].get_rect()
    boton["Rectangulo"].topleft = boton["Posicion"]

    return boton

def dibujar(boton):
    boton["Ventana"].blit(boton["Contenido"], boton["Posicion"])

def dibujar_botones(lista):
    for boton in lista:
        dibujar(boton)
    

def checkear_accion_botones(lista_botones, evento):
    for boton in lista_botones:
        if boton["Rectangulo"].collidepoint(evento.pos):
            boton["Accion"]()