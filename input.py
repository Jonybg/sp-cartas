import pygame
def crear_input(ventana,fuente,color_activo, color_desactivado, posicion, dimensiones):
    input  = {}
    input["Ventana"] = ventana
    input["Fuente"] = pygame.font.SysFont(fuente[0],fuente[1])
    input["Color_activo"] = color_activo
    input["Color_inactivo"] = color_desactivado
    input["Texto"] = ""
    input["Activo"] = False
    input["Posicion"] = posicion
    input["Dimensiones"] = dimensiones
    input["Rectangulo"] = pygame.Rect(posicion[0],posicion[1],dimensiones[0],dimensiones[1])
    input["Color_actual"] = color_desactivado

    return input



def dibujar_input(input):
    superficie = input["Fuente"].render(input["Texto"],False,"Black")
    input["Ventana"].blit(superficie,(input["Rectangulo"].x + 5,input["Rectangulo"].y + 7))
    pygame.draw.rect(input["Ventana"],input["Color_actual"],input["Rectangulo"],2)


def cambiar_color(input):
    input["Activo"] = not input["Activo"]
    if input["Activo"] == True:
        input["Color_actual"] = input["Color_activo"]
    else:
        input["Color_actual"] = input["Color_inactivo"]

def escribir(input, evento):
    if evento.key == pygame.K_RETURN:
        print(f"Texto al presionar Enter: {input['Texto']}")
    elif evento.key == pygame.K_BACKSPACE:
        input["Texto"] = input["Texto"][:-1]
    else:
        input["Texto"] += evento.unicode
    
    print(f"Texto actualizado: {input['Texto']}")
