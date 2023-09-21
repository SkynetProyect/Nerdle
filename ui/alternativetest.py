import random


class Ecuacion:

    def __init__(self):
        print("Clase Ecuacion creada con numeros y operadores random")

        self.numeros: list = [random.randint(0, 9) for _ in range(3)]  # Generar 4 números enteros de 0 a 9
        self.ecuacion: list = []

        if self.numeros[2] == 0:
            self.numeros[2] = 3

        print(f"  numeros generados {self.numeros}")

        self.operadores: list = ["*", "/", "+", "-"]

        print(f"  operadores generados {self.operadores}")

    def confirmar_logica(self, lista: list) -> int:
        print("METODO CONFIRMAR_LOGICA LLAMADO")

        for i in range(len(lista)):
            print("  inicio del bucle for")
            print(f"  objeto a revisar: {lista[i]}")
            if type(lista[i]) != int:
                print(f"   es un {type(lista[i])} Cumplio la condicion de no ser un numero... ")
                if lista[i] == "*":
                    print("   operador detectado * ")
                    lista[i] = lista[i-1] * lista[i+1]
                    print(f"    resultado actual {lista[i]} en la posicion {i}")
                elif lista[i] == "/":
                    print("   operador detectado / ")
                    lista[i] = lista[i - 1] / lista[i + 1]
                    print(f"    resultado actual {lista[i]} en la posicion {i}")
                elif lista[i] == "+":
                    print("   operador detectado + ")
                    lista[i] = lista[i - 1] + lista[i + 1]
                    print(f"    resultado actual {lista[i]} en la posicion {i}")
                elif lista[i] == "-":
                    print("   operador detectado - ")
                    lista[i] = lista[i - 1] - lista[i + 1]
                    print(f"    resultado actual {lista[i]} en la posicion {i}")

                print("  iniciando proceso de borrado de datos ya usados")
                lista.remove(lista[i-1])
                lista.remove(lista[i+1])
            else:
                print("  No cumplio con la condicion inicial, saltando al siguiente")

        print(f" resultado a retornar: {lista[0]}")

        return lista[0]




    def generar_ecuacion(self):

        print("METODO GENERAR_ECUACION LLAMADO")
        self.ecuacion.append(self.numeros[0])
        self.ecuacion.append(random.choice(self.operadores))

        for i in range(1, 2):
            numero: int = self.numeros[i]
            operador: str = random.choice(self.operadores)

            if operador == "/" and numero == 0:  # Evitar la división por cero
                numero = 1

            self.ecuacion.append(numero)
            self.ecuacion.append(operador)

        self.ecuacion.append(self.numeros[2])
        self.ecuacion.append("=")

        print(f"ecuacion generada: {self.ecuacion}")

        self.ecuacion = self.confirmar_logica(self.ecuacion)



inicio = Ecuacion()
inicio.generar_ecuacion()
