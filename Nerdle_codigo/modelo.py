from dataclasses import dataclass
import random

verde = 94, 204, 42
amarillo = 237, 255, 20
gris = 83, 83, 83
gris_claro = 236, 236, 236

@dataclass
class Jugador:
    def registrar_jugador(self):
        nombre_usuario = []
        nombre = input("Ingrese su nombre: ")
        nombre_usuario.append(nombre)

        print("su nombre es:")
        for elemento in nombre_usuario:
            print(elemento)

        correo_usuario = []
        correo = input("Ingrese su correo: ")
        correo_usuario.append(correo)

        print("su correo es:")
        for elemento in correo_usuario:
            print(elemento)

class Ecuacion:
    class Ecuacion:
        def _init_(self):
            self.numeros = [random.randint(0, 9) for _ in range(3)]  # Generar 4 números enteros de 0 a 9
            self.operadores = [random.choice(["+", "-", "*", "/"]) for _ in range(3)]  # Generar 3 operadores
            self.igual = "="

        def generar_ecuacion(self):
            ecuacion = str(self.numeros[0])
            for i in range(2):
                operador = self.operadores[i]
                numero = self.numeros[i + 1]

                if operador == "/" and numero == 0:  # Evitar la división por cero
                    numero = 1

                ecuacion += f" {operador} {numero}"

            resultado = eval(ecuacion)
            self.ecuacion = f"{ecuacion} {self.igual} {int(resultado)}"

    # Crear una instancia de la clase Ecuacion
    ecuacion_obj = Ecuacion()

    # Generar la ecuación
    ecuacion_obj.generar_ecuacion()

    # Imprimir la ecuación
    print(f"Ecuación: {ecuacion_obj.ecuacion}")


class Nerdle:
    def __init__(self):
        self.intentos_maximos = 6
        self.intentos_realizados = 0
        self.ecuacion_generada = Ecuacion().generar_ecuacion()

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
