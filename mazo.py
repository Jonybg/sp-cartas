import random

def cargar_mazo(path):
    mazo = []
    with open(path, "r") as archivo:
        contenido = archivo.readlines()
        contenido.pop(0)
        for linea in contenido:
            valores = linea.strip().split(",")
            carta = {
                "nombre": valores[0],
                "velocidad": int(valores[1]),
                "fuerza": int(valores[2]),
                "elemento": valores[3],
                "peso": float(valores[4]),
                "altura": float(valores[5])
            }
            mazo.append(carta)
    return mazo


    
def mezclar_mazo(mazo: list) -> list:
    '''Mezcla el mazo usando el algoritmo de Fisher-Yates y lo devuelve'''
    for i in range(len(mazo) - 1, 0, -1):
        j = random.randint(0, i)  
        mazo[i], mazo[j] = mazo[j], mazo[i]  
    return mazo

def repartir_cartas(mazo: list) -> dict:
    '''Creamos un diccionario para guardar las cartas de cada jugador'''
    mazos = {
        "jugador1": [],
        "jugador2": []
    }
    '''Repartimos las cartas entre los jugadores
       teniendo en cuenta si el indice es par o impar'''
    for i in range(len(mazo)):
        if i % 2 == 0:
            mazos["jugador1"].append(mazo[i])  
        else:
            mazos["jugador2"].append(mazo[i])  

    return mazos