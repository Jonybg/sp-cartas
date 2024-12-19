import pygame
from juego_pygame import *
from ordenamiento import *  
from configuraciones import *  
from input import *  
from boton import * 
from juego import *  
from pantallas import *

pygame.init()
pygame.mixer.init()
def main_pygame():
    ventana_ppal, fondo = inicializar_ventana()
    lista_botones = crear_botones_dinamicos(ventana_ppal)
    input_width = 400
    input_height = 50
    center_x = (ventana_ppal.get_width() - input_width) // 2
    input1_pos = (center_x, 200)
    input2_pos = (center_x, 300)
    input1 = crear_input(ventana_ppal, ("consolas", 30), "Red", "Blue", input1_pos, (input_width, input_height))
    input2 = crear_input(ventana_ppal, ("consolas", 30), "Red", "Blue", input2_pos, (input_width, input_height))
    input_activo = ""
    fase = "inicio"
    flag_run = True
    jugadores = {}
    reproducir_musica()
    while flag_run:
        ventana_ppal.fill((0, 0, 0))  
        ventana_ppal.blit(fondo, (0, 0))
        boton_sonido = toggle_sound_button(ventana_ppal)
        data = manejador_eventos(lista_botones, input1, input2, input_activo, fase, jugadores, ventana_ppal, boton_sonido)
        flag_run = data["flag_run"]
        input_activo = data["input_activo"]
        fase = data["fase"]
        jugadores =data["jugadores"]
        if fase == "inicio":
            jugadores = {}
            pantalla_inicio(ventana=ventana_ppal, fondo=fondo, lista_botones=lista_botones)
        elif fase == "ingresar_nombres":
            pantalla_ingresar_nombres(ventana_ppal, fondo, input1, input2, jugadores, input1_pos, input2_pos)
        elif fase == "jugando":
            datos_jugadores = preparar_datos_jugadores(jugadores)
            mazo_jugadores = preparar_mazo()
            fase = jugar_con_pygame(datos_jugadores, mazo_jugadores) 
        elif fase == "ranking":
            pantalla_ranking(ventana_ppal, fondo)        
        pygame.display.flip()      
    pygame.quit()

main_pygame()
# def main():
#     '''Funcion principal del programa'''
#     while True:
#         opcion = input("1: Jugar 2:Ranking 3: Salir: ")
#         match opcion:
#             case "1":
#                 ejecutar_juego()
#             case "2":
#                 criterio = input("¿Por qué criterio deseas ordenar? (puntuacion/Victorias Elementales): ")
#                 orden = input("¿En qué orden deseas ver el ranking? (asc/desc): ")
#                 ordenar(criterio, orden)  
#             case "3":
#                 print("Saliendo...")
#                 break
#             case _:
#                 print("Opción inválida")
        
# main()