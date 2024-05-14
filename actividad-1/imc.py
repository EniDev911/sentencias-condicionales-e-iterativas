import sys

"""
   - Bajo Peso: < 18.5
   - Adecuado: 18.5 - 25
   - Sobrepeso: 25 - 30
   - Obesidad grado I: 30 - 35
   - Obesidad grado II: 35 - 40
   - Obesidad grado III: Más de 40
"""

if len(sys.argv) == 3:

    peso = float(sys.argv[1])
    altura = float(sys.argv[2]) / 100

    nivel_de_peso = round(peso / (altura * altura), 2)
    clasificacion = "Su IMC es %s\nLa clasificación OMS es %s"

    if nivel_de_peso <= 18.5:
        print(clasificacion % (nivel_de_peso, "Bajo Peso"))
    elif nivel_de_peso <= 25:
        print(clasificacion % (nivel_de_peso, "Adecuado"))
    elif nivel_de_peso <= 30:
        print(clasificacion % (nivel_de_peso, "Sobrepeso"))
    elif nivel_de_peso <= 35:
        print(clasificacion % (nivel_de_peso, "Obesidad Grado I"))
    elif nivel_de_peso <= 40:
        print(clasificacion % (nivel_de_peso, "Obesidad Grado II"))
    else:
        print(clasificacion % (nivel_de_peso, "Obesidad Grado III"))

else:
    msg = "Debes pasarme los argumentos peso y altura por línea de comandos"
    print(msg + "\nEj: python imc.py 81 178")
