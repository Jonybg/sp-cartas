import random
from mazo import *
from jugadores import *

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
    retorno = "Empate"
    if atributo == "elemento":
        retorno = comparar_elementos(carta1["elemento"], carta2["elemento"])  
    else:
        if carta1[atributo] > carta2[atributo]:
                retorno =  "carta1"  
        elif carta2[atributo] > carta1[atributo]:
                retorno =  "carta2"  
    return retorno


def comparar_elementos(elemento1, elemento2):
    retorno = "Empate"  
    
    for elemento in tabla_debilidades:
        if elemento["elemento"] == elemento1 and elemento["debilidad"] == elemento2:
            retorno = "carta2"  
            break  
        elif elemento["elemento"] == elemento2 and elemento["debilidad"] == elemento1:
            retorno = "carta1"  
            break  

    return retorno




def agregar_cartas_a_mazo(mazo, carta1, carta2):
    mazo.extend([carta1, carta2])
