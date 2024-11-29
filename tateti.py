import random
from mazo import *  

def obtener_cartas_jugadores(carta1, carta2):
    elementos_ronda_actual = [carta1["elemento"], carta2["elemento"]]
    return elementos_ronda_actual

def crear_tablero(elementos, filas_restantes, columnas, tablero=None):
    if tablero == None:
        tablero = []
    if filas_restantes == 0:
        return tablero
    fila_actual = []
    for i in range(columnas):
        fila_actual.append(random.choice(elementos))

    tablero.append(fila_actual)
    return crear_tablero(elementos, filas_restantes - 1, columnas, tablero)


def imprimir_tablero(tablero):
    for fila in tablero:
        print(" | ".join(fila))
        print("-" * 5)


def verificar_filas(tablero, elemento):
    combinaciones = 0
    for i in range(len(tablero)):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] == elemento:
            combinaciones += 1
    return combinaciones

def verificar_columnas(tablero, elemento):
    combinaciones = 0
    for j in range(len(tablero[0])):
        if tablero[0][j] == tablero[1][j] == tablero[2][j] == elemento:
            combinaciones += 1
    return combinaciones

def verificar_diagonal_principal(tablero, elemento):
    combinaciones = 1  
    for i in range(len(tablero)):  
        if tablero[i][i] != elemento:  
            combinaciones = 0  
            break  
    return combinaciones  


def verificar_diagonal_secundaria(tablero, elemento):
    combinaciones = 1 
    for i in range(len(tablero)):  
        if tablero[i][len(tablero) - i - 1] != elemento: 
            combinaciones = 0  
            break  
    return combinaciones 

def verificar_combinaciones(tablero, elemento):

    combinaciones = 0

    filas_combinaciones = verificar_filas(tablero, elemento)
    combinaciones += filas_combinaciones  
    
    
    columnas_combinaciones = verificar_columnas(tablero, elemento)
    combinaciones += columnas_combinaciones 
    

    diagonal_principal_combinaciones = verificar_diagonal_principal(tablero, elemento)
    combinaciones += diagonal_principal_combinaciones 
    
   
    diagonal_secundaria_combinaciones = verificar_diagonal_secundaria(tablero, elemento)
    combinaciones += diagonal_secundaria_combinaciones  

    return combinaciones


def bubble_sort(combinaciones):
    for i in range(len(combinaciones) - 1):
        for j in range(i + 1, len(combinaciones)):
            if combinaciones[i][2] < combinaciones[j][2]:  
                combinaciones[i], combinaciones[j] = combinaciones[j], combinaciones[i]
    return combinaciones

def mostrar_combinaciones(combinaciones_ordenadas):
    print(f"{combinaciones_ordenadas[0][0]} ({combinaciones_ordenadas[0][1]}) tiene {combinaciones_ordenadas[0][2]} combinaciones ganadoras.")
    print(f"{combinaciones_ordenadas[1][0]} ({combinaciones_ordenadas[1][1]}) tiene {combinaciones_ordenadas[1][2]} combinaciones ganadoras.")

def anunciar_ganador_o_empate(combinaciones_ordenadas):
    if combinaciones_ordenadas[0][2] == combinaciones_ordenadas[1][2]:
        print("¡Empate! Ambos jugadores tienen el mismo número de combinaciones ganadoras.")
    else:
        print(f"El jugador con más combinaciones ganadoras es: {combinaciones_ordenadas[0][0]} con {combinaciones_ordenadas[0][2]} combinaciones.")

def mostrar_resultado_final(combinaciones_jugador1, combinaciones_jugador2, nombre_jugador1, nombre_jugador2):
    if combinaciones_jugador1 > combinaciones_jugador2:
        print(f"¡{nombre_jugador1} gana con {combinaciones_jugador1} combinaciones ganadoras!")
    elif combinaciones_jugador2 > combinaciones_jugador1:
        print(f"¡{nombre_jugador2} gana con {combinaciones_jugador2} combinaciones ganadoras!")
    else:
        print(f"¡Empate! Ambos jugadores tienen el mismo número de combinaciones ganadoras.")

def determinar_ganador(combinaciones_ordenadas, combinaciones_jugador1, combinaciones_jugador2, nombre_jugador1, nombre_jugador2):
    mostrar_combinaciones(combinaciones_ordenadas)
    anunciar_ganador_o_empate(combinaciones_ordenadas)
    mostrar_resultado_final(combinaciones_jugador1, combinaciones_jugador2, nombre_jugador1, nombre_jugador2)






def jugar_tateti(carta1, carta2, datos_jugadores):
    elementos = obtener_cartas_jugadores(carta1, carta2)
    tablero = crear_tablero(elementos, filas_restantes=3, columnas=3)
    jugador1 = elementos[0]
    jugador2 = elementos[1]
    nombre_jugador1 = datos_jugadores["jugador1"]["nombre"]
    nombre_jugador2 = datos_jugadores["jugador2"]["nombre"] 
    combinaciones_jugador1 = verificar_combinaciones(tablero, jugador1)
    combinaciones_jugador2 = verificar_combinaciones(tablero, jugador2)
    print("Tablero:")
    imprimir_tablero(tablero)
    combinaciones = [
        (nombre_jugador1, jugador1, combinaciones_jugador1),
        (nombre_jugador2, jugador2, combinaciones_jugador2)
    ]
    combinaciones_ordenadas = bubble_sort(combinaciones)
    
    determinar_ganador(combinaciones_ordenadas, combinaciones_jugador1, combinaciones_jugador2, nombre_jugador1, nombre_jugador2)



