import pygame

def crear_boton(ventana,posicion,dimensiones,fuente=None,texto=None,path_imagen=None,opacidad=255):
    boton = {}
    boton["Ventana"] = ventana
    boton["Posicion"] = posicion
    boton["Dimensiones"] = dimensiones
    boton["Texto"] = texto
    boton["Fuente"] = fuente
    boton["Presionado"] = False

    if path_imagen != None:
     superficie_imagen = pygame.image.load(path_imagen)
     boton["Superficie"] = pygame.transform.scale(superficie_imagen,boton["Dimensiones"])
     boton["Superficie"].set_alpha(opacidad)
    else:
       pass

    boton["Rectangulo"] = boton["Superficie"].get_rect()
    boton["Rectangulo"].topleft = boton["Posicion"]

    return boton



def dibujar(boton):
   boton["Ventana"].blit(boton["Superficie"],boton["Posicion"])
   if boton["Texto"] and boton["Fuente"]:
        texto_superficie = boton["Fuente"].render(boton["Texto"], True, (0, 0, 0))  # Texto en color negro
        texto_rect = texto_superficie.get_rect(center=boton["Rectangulo"].center)  # Centrar texto en el botón
        boton["Ventana"].blit(texto_superficie, texto_rect)