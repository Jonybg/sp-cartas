from juego import ejecutar_juego

def main():
    while True:
        opcion = input("1: Jugar 2: Salir: ")
        match opcion:
            case "1":
                ejecutar_juego()
            case "2":
                print("Saliendo...")
                break
            case _:
                print("Opción inválida")
        
main()






