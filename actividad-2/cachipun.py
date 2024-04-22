import sys
import random

opcion_usuario = sys.argv[1]
opciones = ["Piedra", "Papel", "Tijera"]                    
opcion_computador = random.choice(opciones)

if not opcion_usuario or not opcion_usuario in opciones:
    print("Debes jugar una opción válida.")
    print(f"Opciones válidas: {opciones}.")
    print("Ejemplo: $ python cachipun.py", random.choice(opciones))

else: 
    if opcion_usuario == opcion_computador:
        print(f"Tú haz elegido {opcion_usuario} y el computador {opcion_computador}. Empate")

    elif (opciones.index(opcion_usuario) == 0 and opciones.index(opcion_computador) == 2):
        print(
            f"Tú haz elegido {opcion_usuario} y el computador {opcion_computador}. Ganaste"
        )

    elif (opciones.index(opcion_usuario) == 1 and opciones.index(opcion_computador) == 0):
        print(
            f"Tú haz elegido {opcion_usuario} y el computador {opcion_computador}. Ganaste"
        )

    elif (opciones.index(opcion_usuario) == 2 and opciones.index(opcion_computador) == 1):
        print(
            f"Tú haz elegido {opcion_usuario} y el computador {opcion_computador}. Ganaste"
        )

    else:
        print(f"Tú haz elegido {opcion_usuario} y el computador {opcion_computador}. Perdiste")
