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
    random.shuffle(mazo)
    return mazo




def dividir_mazo(mazo):
    mitad = len(mazo) // 2
    mazo_jugadores = {
        "jugador1": mazo[:mitad],
        "jugador2": mazo[mitad:]
    }
    return mazo_jugadores