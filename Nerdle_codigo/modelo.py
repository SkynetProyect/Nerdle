import random

verde = 94, 204, 42
amarillo = 237, 255, 20
gris = 83, 83, 83
gris_claro = 236, 236, 236

""" Se genera la clase jugador la cual con tiene la funcion de iniciacion y los metodos registrar nombre y registrar
correo. """


class Jugador:
    """ El metodo init crea la clase jugador asignandole dos variables que contiene el nombre y el correo """

    def __init__(self):
        self.nombre_jugador: str = ""
        self.correo_jugador: str = ""

        print(" Clase Jugador iniciada")

    """El metodo registrar nombre del jugador recibe el nombre y se lo asigna al jugador, retornando el nombre 
    recibido """

    def registrar_nombre_jugador(self, nombre_jugador: str) -> str:
        self.nombre_jugador = nombre_jugador
        print(f" Nombre de jugador asignado en clase jugador con nombre {str(self.nombre_jugador)}")
        return self.nombre_jugador

    """ La metodo correo del jugador recibe el nombre y se lo asigna al jugador, retornando el nombre recibido"""

    def registrar_correo_jugador(self, correo_jugador: str) -> str:
        print(f" Correo de jugador asignado en clase jugador con entrada {str(self.correo_jugador)}")
        self.correo_jugador = correo_jugador
        return self.correo_jugador


""" Clase Ecuacion """


class Ecuacion:
    def _init_(self):
        self.numeros: list = [random.randint(0, 9) for _ in range(3)]  # Generar 3 números enteros de 0 a 9
        self.operadores: list = [random.choice(["+", "-", "*", "/"]) for _ in range(3)]  # Generar 3 operadores
        self.ecuacion: str = ""
        print("Clase Ecuacion creada con numeros y operadores random")

    def generar_ecuacion(self):

        print(" metodo generar_ecuacion llamado")
        ecuacion = f"{self.numeros[0]} + {self.operadores[0]}"
        for i in range(1, 3):
            operador: str = self.operadores[i]
            numero: int = self.numeros[i]

            if operador == "/" and numero == 0:  # Evitar la división por cero
                numero = 1

            ecuacion += f" {operador} {numero}"
        ecuacion += "="
        print(f"ecuacion generada: {ecuacion}")

        self.ecuacion = ecuacion



class Nerdle:
    def __init__(self):
        self.intentos_maximos: int = 6
        self.intentos_realizados: int = 0
        self.ecuacion: Ecuacion = Ecuacion()


    def numero_intentos(self):
        while self.intentos_realizados < self.intentos_maximos:
            adivinanza = input(f"Intento {self.intentos_realizados + 1}/{self.intentos_maximos}: Adivina la ecuacion: ")
            resultado = Ecuacion().generar_ecuacion()[1]
            if float(adivinanza) == resultado:
                print("¡Adivinaste la ecuación, ganaste!")
            else:
                self.intentos_realizados += 1
                print(f"Intento {self.intentos_realizados}/{self.intentos_maximos}: Sigue intentando.")
        else:
            print("se te acabaron los intentos, lo siento perdiste")

    limite_intentos = numero_intentos()

    def comprobar_ecuacion(self, ecuacion_recibida, ecuacion_generada):
        if ecuacion_recibida.ecuacion == ecuacion_generada.ecuacion:
            return True
        else:
            return self.limite_intentos

    def estado_juego(self):
        pass

    def anunciar_resultado(self):
        pass


class Estadistica:

    def registar_datos(self):
        pass

    def actualizar_estadisticas(self):
        pass

    def enviar_estadisticas(self):
        pass


class Retroalimentacion:
    def revisar_congruencia(self):
        pass

    def retroalimentar(self, ecuacion_original, ecuacion_recibida):
        color_codigo = [gris_claro, gris_claro, gris_claro, gris_claro, gris_claro, gris_claro, gris_claro, gris_claro]

        for x in range(0, 8):
            if ecuacion_original[x] == ecuacion_recibida[x]:
                color_codigo[x] = verde
            if ecuacion_recibida[x] in ecuacion_original:
                color_codigo[x] = amarillo
            else:
                color_codigo[x] = gris

        return color_codigo


juego = Nerdle()
juego.numero_intentos()
