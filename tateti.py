import random
from mazo import *  

def obtener_cartas_jugadores(carta1: dict, carta2: dict) -> list:
    '''Obtiene los elementos de las cartas de cada jugador y lo devuelve'''
    elementos_ronda_actual = [carta1["elemento"], carta2["elemento"]]                                                             
    return elementos_ronda_actual

def crear_tablero(elementos: list, filas_restantes: int, columnas: int, tablero=None) -> list:
    '''Crea el tablero si no se le pasa uno como argumento'''
    if tablero == None:
        tablero = []
    '''Si las filas restantes son 0, devolvemos el tablero'''
    if filas_restantes == 0:
        return tablero
    '''Si no, creamos una fila con elementos aleatorios y la añadimos al tablero'''
    fila_actual = []
    for i in range(columnas):
        fila_actual.append(random.choice(elementos))
    '''Añadimos la fila al tablero y llamamos a la funcion recursivamente, hasta que las filas restantes sean 0'''
    tablero.append(fila_actual)
    return crear_tablero(elementos, filas_restantes - 1, columnas, tablero)


def imprimir_tablero(tablero: list) -> None:
    '''Printeamos el tablero'''
    for fila in tablero:
        print(" | ".join(fila))
        print("-" * 5) 


def verificar_filas(tablero: list, elemento: list) -> int:
    '''Verificamos si hay combinaciones ganadoras en las filas y devolvemos las mismas'''
    combinaciones = 0
    for i in range(len(tablero)):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] == elemento:
            combinaciones += 1
    return combinaciones

def verificar_columnas(tablero: list, elemento: list) -> int:
    '''Verificamos si hay combinaciones ganadoras en las columnas y devolvemos las mismas'''
    combinaciones = 0
    for j in range(len(tablero[0])):
        if tablero[0][j] == tablero[1][j] == tablero[2][j] == elemento:
            combinaciones += 1
    return combinaciones

def verificar_diagonal_principal(tablero: list, elemento: list) -> int:
    '''Verificamos si hay combinaciones ganadoras en la diagonal principal y devolvemos las mismas'''
    combinaciones = 1  
    for i in range(len(tablero)):
        if tablero[i][i] != elemento:  
            combinaciones = 0  
            break  
    return combinaciones  


def verificar_diagonal_secundaria(tablero: list, elemento: list) -> int:
    '''Verificamos si hay combinaciones ganadoras en la diagonal secundaria y devolvemos las mismas'''
    combinaciones = 1 
    for i in range(len(tablero)):  
        if tablero[i][len(tablero) - i - 1] != elemento: 
            combinaciones = 0  
            break  
    return combinaciones 

def verificar_combinaciones(tablero: list, elemento: list) -> int:
    '''Verificamos si hay combinaciones ganadoras en el tablero y devolvemos las mismas'''
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


def bubble_sort(combinaciones: list) -> list:
    '''Ordenamos las combinaciones de mayor a menor'''
    for i in range(len(combinaciones) - 1):
        for j in range(i + 1, len(combinaciones)):
            if combinaciones[i][2] < combinaciones[j][2]:  
                combinaciones[i], combinaciones[j] = combinaciones[j], combinaciones[i]
    return combinaciones

def mostrar_combinaciones(combinaciones_ordenadas: list) -> None:
    '''Mostramos las combinaciones de mayor a menor'''
    print(f"{combinaciones_ordenadas[0][0]} ({combinaciones_ordenadas[0][1]}) tiene {combinaciones_ordenadas[0][2]} combinaciones ganadoras.")
    print(f"{combinaciones_ordenadas[1][0]} ({combinaciones_ordenadas[1][1]}) tiene {combinaciones_ordenadas[1][2]} combinaciones ganadoras.")

def determinar_resultado_final(combinaciones_jugador1: int, combinaciones_jugador2: int) -> str:
    '''Determinamos quien tiene mas combinaciones ganadoras o si hay empate'''
    ganador = None
    if combinaciones_jugador1 > combinaciones_jugador2:
        ganador =  "jugador1"
    elif combinaciones_jugador2 > combinaciones_jugador1:
        ganador =  "jugador2"
    else:
        ganador= "empate"
    return ganador

def determinar_ganador(combinaciones_ordenadas: list, combinaciones_jugador1: int, combinaciones_jugador2: int) -> str:
    '''Printeamos y determinamos el ganador'''
    mostrar_combinaciones(combinaciones_ordenadas)
    ganador = determinar_resultado_final(combinaciones_jugador1, combinaciones_jugador2)
    return ganador


def jugar_tateti(carta1: list, carta2: list, datos_jugadores: dict) -> str:
    '''Funcion principal del tateti'''
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
    
    resultado = determinar_ganador(combinaciones_ordenadas, combinaciones_jugador1, combinaciones_jugador2)
    return resultado



