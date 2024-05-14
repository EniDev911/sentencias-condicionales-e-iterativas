import sys
import random

if len(sys.argv) == 2:

    opcion_usuario = sys.argv[1].lower()

    if (opcion_usuario == "piedra" or
            opcion_usuario == "papel" or
            opcion_usuario == "tijera"):

        aleatorio = random.randint(1, 3)

        if aleatorio == 1:
            opcion_computador = "piedra"
        elif aleatorio == 2:
            opcion_computador = "papel"
        elif aleatorio == 3:
            opcion_computador = "tijera"

        if opcion_usuario == opcion_computador:
           print(f"Tú haz elegido {opcion_usuario} y el computador {opcion_computador}. Empate")

        elif ((opcion_usuario == "piedra" and opcion_computador == "tijera") or
                (opcion_usuario == "papel" and opcion_computador == "piedra") or
                (opcion_usuario == "tijera" and opcion_computador == "papel")):
            print(f"Tú haz elegido {opcion_usuario} y el computador {opcion_computador}. Ganaste")

        else:
            print(f"Tú haz elegido {opcion_usuario} y el computador {opcion_computador}. Perdiste")

    else:
        print("Debes jugar una opción válida.")
        print("Opciones válidas: Piedra, Papel, Tijera.")
        print("Ejemplo: $ python cachipun.py", "tijera")
        exit()

else:
    print("Debes pasarme el argumento por línea de comando")