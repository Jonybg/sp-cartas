import json

def obtener_nombres_jugadores():
    datos_jugadores = {}
    for i in range(1, 3):
        nombre = ""
        while len(nombre.strip()) == 0:
            nombre = input(f"Ingrese el nombre del jugador {i}: ")
            if len(nombre.strip()) == 0:
                print("El nombre no puede estar vacio. Try again.")
        datos_jugadores[f"jugador{i}"] = {"nombre": nombre.strip(), "puntuacion": 0}
    return datos_jugadores
    

def guardar_datos_jugadores(datos_jugadores):
    archivo_json = "datos_jugadores.json"

    with open(archivo_json, "w") as archivo:
        json.dump(datos_jugadores, archivo, indent=4)