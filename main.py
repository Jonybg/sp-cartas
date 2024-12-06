from juego import *
from ordenamiento import *
import pygame
from boton import *
from funciones_pygame import *
from configuraciones import *
from input import *
pygame.mixer.init()

def reproducir_musica():
    pygame.mixer.music.load("intro.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

def manejador_eventos(lista_botones, input1, input2, input_activo, fase, jugadores):
    flag_run = True
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            flag_run = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            checkear_accion_botones(lista_botones, evento)
            
            if fase == "inicio":
                if lista_botones[0]["Rectangulo"].collidepoint(evento.pos): 
                    fase = "ingresar_nombres"  
            elif fase == "ingresar_nombres":
                if input1["Rectangulo"].collidepoint(evento.pos):
                    cambiar_color(input1)
                    input_activo = "input1" 
                elif input2["Rectangulo"].collidepoint(evento.pos):
                    cambiar_color(input2)
                    input_activo = "input2" 
        elif evento.type == pygame.KEYDOWN:
            if input_activo == "input1" and input1["Activo"]:
                escribir(input1, evento)
            elif input_activo == "input2" and input2["Activo"]:
                escribir(input2, evento)

        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_RETURN:
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

            if jugadores.get("jugador1") and jugadores.get("jugador2"):
                fase = "jugando"  

    return flag_run, input_activo, fase, jugadores


def main_pygame():
    ventana_ppal, fondo = inicializar_ventana()
    lista = crear_botones_dinamicos(ventana_ppal)  
    
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
        flag_run, input_activo, fase, jugadores = manejador_eventos(lista, input1, input2, input_activo, fase, jugadores)

        if fase == "inicio":
            ventana_ppal.blit(fondo, (0, 0))
            dibujar_botones(lista)
        elif fase == "ingresar_nombres":
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
        elif fase == "jugando":
            ventana_ppal.fill((0, 0, 0))  
            fuente = pygame.font.SysFont("consolas", 40)

            mensaje_jugando = fuente.render("¡Jugando!", True, (255, 255, 255))
            texto_jugador1 = fuente.render(f"Jugador 1: {jugadores.get('jugador1', 'No asignado')}", True, (255, 255, 255))
            texto_jugador2 = fuente.render(f"Jugador 2: {jugadores.get('jugador2', 'No asignado')}", True, (255, 255, 255))


            ventana_ppal.blit(mensaje_jugando, (ventana_ppal.get_width() // 2 - mensaje_jugando.get_width() // 2, ventana_ppal.get_height() // 4))
            ventana_ppal.blit(texto_jugador1, (ventana_ppal.get_width() // 2 - texto_jugador1.get_width() // 2, ventana_ppal.get_height() // 2 - 40))
            ventana_ppal.blit(texto_jugador2, (ventana_ppal.get_width() // 2 - texto_jugador2.get_width() // 2, ventana_ppal.get_height() // 2 + 40))

        pygame.display.update()

    pygame.quit()


main_pygame()


def main():
    '''Funcion principal del programa'''
    while True:
        opcion = input("1: Jugar 2:Ranking 3: Salir: ")
        match opcion:
            case "1":
                ejecutar_juego()
            case "2":
                criterio = input("¿Por qué criterio deseas ordenar? (puntuacion/Victorias Elementales): ")
                orden = input("¿En qué orden deseas ver el ranking? (asc/desc): ")
                ordenar(criterio, orden)  
            case "3":
                print("Saliendo...")
                break
            case _:
                print("Opción inválida")
        
main()
