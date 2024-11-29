import random

def cargar_mazo(path: str) -> list:
    '''Carga el mazo desde un archivo CSV'''
    with open(path, "r") as archivo:
        return [
            {
                "nombre": valores[0],
                "velocidad": int(valores[1]),
                "fuerza": int(valores[2]),
                "elemento": valores[3],
                "peso": float(valores[4]),
                "altura": float(valores[5])
            }
            for valores in (line.split(",") for line in archivo.readlines()[1:])
        ]
    
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