import random


class Ecuacion:

    def __init__(self):
        print("Clase Ecuacion creada con numeros y operadores random")
        self.numeros: list = [random.randint(0, 9) for _ in range(3)]  # Generar 4 números enteros de 0 a 9

        if self.numeros[2] == 0:
            self.numeros[2] = 3

        print(f"  numeros generados {self.numeros}")
        self.operadores: list = ["+", "-", "*", "/"]
        print(f"  operadores generados {self.operadores}")
        self.ecuacion: str = ""

    def generar_ecuacion(self):

        print(" metodo generar_ecuacion llamado")
        ecuacion = f"{self.numeros[0]}{random.choice(self.operadores)}"

        for i in range(1, 2):
            numero: int = self.numeros[i]
            operador: str = random.choice(self.operadores)

            if operador == "/" and numero == 0:  # Evitar la división por cero
                numero = 1

            ecuacion += f" {numero}{operador}"

        ecuacion += f"{self.numeros[2]}="
        print(f"ecuacion generada: {ecuacion}")

        self.ecuacion = ecuacion

inicio = Ecuacion()
inicio.generar_ecuacion()
