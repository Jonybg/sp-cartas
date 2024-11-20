import random

tabla_debilidades = [
    {"elemento": "Tierra", "debilidad": "Aire"},
    {"elemento": "Electricidad", "debilidad": "Tierra"},
    {"elemento": "Agua", "debilidad": "Electricidad"},
    {"elemento": "Fuego", "debilidad": "Agua"},
    {"elemento": "Aire", "debilidad": "Fuego"}
]

atributos = ["velocidad", "fuerza", "elemento", "peso", "altura"]

def elegir_atributo_aleatorio():
    return random.choice(atributos)

def comparar_cartas(carta1, carta2, atributo):
    if atributo == "elemento":
        return comparar_elementos(carta1["elemento"], carta2["elemento"])
    else:
        if carta1[atributo] > carta2[atributo]:
            return "carta1"
        elif carta2[atributo] > carta1[atributo]:
            return "carta2"
        else:
            return "Empate"

def comparar_elementos(elemento1, elemento2):
    for elemento in tabla_debilidades:
        if elemento["elemento"] == elemento1 and elemento["debilidad"] == elemento2:
            return "carta2"
        elif elemento["elemento"] == elemento2 and elemento["debilidad"] == elemento1:
            return "carta1"

    return "Empate"

def agregar_cartas_a_mazo(mazo, carta1, carta2):
    mazo.extend([carta1, carta2])
