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

def incrementar_si_valido(condicion: bool, contador: int) -> int:

    if condicion:
        contador += 1
    return contador

def es_valido(celda: str, elemento: str) -> bool:

    return celda == elemento

def verificar_condicion(celda: str, elemento: str, estado_actual: bool) -> bool:
    resultado = False
    if estado_actual and es_valido(celda, elemento):
        resultado = True
    return resultado


def verificar_filas_y_diagonales(tablero: list, elemento: str) -> int:
    combinaciones = 0
    n = len(tablero)
    diagonal_principal = True
    diagonal_secundaria = True

    for i in range(n):
        fila_valida = True
        for j in range(n):
            fila_valida = verificar_condicion(tablero[i][j], elemento, fila_valida)
        combinaciones = incrementar_si_valido(fila_valida, combinaciones)

        diagonal_principal = verificar_condicion(tablero[i][i], elemento, diagonal_principal)
        diagonal_secundaria = verificar_condicion(tablero[i][n - 1 - i], elemento, diagonal_secundaria)

    combinaciones = incrementar_si_valido(diagonal_principal, combinaciones)
    combinaciones = incrementar_si_valido(diagonal_secundaria, combinaciones)

    return combinaciones

def verificar_columnas(tablero: list, elemento: str) -> int:
    '''Verifica las combinaciones ganadoras en columnas.'''
    combinaciones = 0
    n = len(tablero)

    for j in range(n):
        columna_valida = True
        for i in range(n):
            columna_valida = verificar_condicion(tablero[i][j], elemento, columna_valida)
        combinaciones = incrementar_si_valido(columna_valida, combinaciones)

    return combinaciones

def verificar_combinaciones_totales(tablero: list, elemento: str) -> int:
    '''Suma las combinaciones ganadoras de filas, columnas y diagonales.'''
    combinaciones_totales = verificar_filas_y_diagonales(tablero, elemento)
    combinaciones_totales += verificar_columnas(tablero, elemento)
    return combinaciones_totales

def bubble_sort(combinaciones: list) -> list:
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
    '''Determinamos quien tiene más combinaciones ganadoras o si hay empate'''
    if combinaciones_jugador1 > combinaciones_jugador2:
        return "jugador1"
    elif combinaciones_jugador2 > combinaciones_jugador1:
        return "jugador2"
    else:
        return "empate"

def determinar_ganador(combinaciones_ordenadas: list, combinaciones_jugador1: int, combinaciones_jugador2: int) -> str:
    '''Printeamos y determinamos el ganador'''
    mostrar_combinaciones(combinaciones_ordenadas)
    return determinar_resultado_final(combinaciones_jugador1, combinaciones_jugador2)

def jugar_tateti(carta1: list, carta2: list, datos_jugadores: dict) -> str:
    '''Función principal del tateti'''
    elementos = obtener_cartas_jugadores(carta1, carta2)
    tablero = crear_tablero(elementos, filas_restantes=3, columnas=3)
    jugador1 = elementos[0]
    jugador2 = elementos[1]
    nombre_jugador1 = datos_jugadores["jugador1"]["nombre"]
    nombre_jugador2 = datos_jugadores["jugador2"]["nombre"] 
    
    combinaciones_jugador1 = verificar_combinaciones_totales(tablero, jugador1)
    combinaciones_jugador2 = verificar_combinaciones_totales(tablero, jugador2)
    
    print("Tablero:")
    imprimir_tablero(tablero)
    
    combinaciones = [
        (nombre_jugador1, jugador1, combinaciones_jugador1),
        (nombre_jugador2, jugador2, combinaciones_jugador2)
    ] 
    
    combinaciones_ordenadas = bubble_sort(combinaciones)
    return determinar_ganador(combinaciones_ordenadas, combinaciones_jugador1, combinaciones_jugador2)