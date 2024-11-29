import random

def cargar_mazo(path):
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

def mezclar_mazo(mazo):
    for i in range(len(mazo) - 1, 0, -1):
        j = random.randint(0, i)  
        mazo[i], mazo[j] = mazo[j], mazo[i]  
    return mazo

def repartir_cartas(mazo):
    mazos = {
        "jugador1": [],
        "jugador2": []
    }
    for i in range(len(mazo)):
        if i % 2 == 0:
            mazos["jugador1"].append(mazo[i])  
        else:
            mazos["jugador2"].append(mazo[i])  

    return mazos