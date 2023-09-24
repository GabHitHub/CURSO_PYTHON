nombres = ["juan", "relak", "sofia", "gabriel", "lucas"]

def buscarNombre():
    while True:
        nombreElegido = input("Coloque un nombre para ver si está en la lista (o escriba 'salir' para salir): ")
        if nombreElegido.lower() == 'salir':
            break
        elif nombreElegido in nombres:
            print(f"{nombreElegido} está en la lista.")
        else:
            print(f"{nombreElegido} no está en la lista.")

buscarNombre()

