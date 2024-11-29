from juego import ejecutar_juego
import pygame

# pygame.init()
# MEDIDAS = (500,500)
# pygame.display.set_mode(MEDIDAS)
# pygame.display.set_caption("POKEMON CARDS")
# icono = pygame.image.load("pokemon_icono.png")
# pygame.display.set_icon(icono)
# flag = True

# while flag:
#     lista_eventos = pygame.event.get()
#     for evento in lista_eventos:
#         if evento.type == pygame.QUIT:
#             flag = False
#     pygame.display.update()
# pygame.quit()

def main():
    '''Funcion principal del programa'''
    while True:
        opcion = input("1: Jugar 2: Salir: ")
        match opcion:
            case "1":
                ejecutar_juego()
            case "2":
                print("Saliendo...")
                break
            case _:
                print("Opción inválida")
        
main()






