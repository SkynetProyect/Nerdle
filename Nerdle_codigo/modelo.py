from dataclasses import dataclass
import random


@dataclass

class Jugador:
    def registrar_jugador(self):
        pass # no seria con una base de datos?

class Nerdle:
    def comprobar_ecuacion(self):
        pass

    def numero_intentos(self):
        pass

    def estado_juego(self):
        pass

    def anunciar_resultado(self):
        pass

class Estadistica:

    def registar_datos(self):
        pass

    def actualizar_estadisticas(self):
        pass # es necesario?

    def enviar_estadisticas(self):
        pass

class Ecuacion:

    def generar_ecuacion(self,):
        ecuacion = dict(numeros=[random.randint(0, 9) for _ in range(8)],
                        operadores=[random.choice(["+", "-", "*", "/"]) for _ in range(7)])
        ecuacion = f"{dict:numeros[0]}"
        for i in range(7):
            ecuacion += f" {dict:operadores[i]} {dict:numeros[i + 1]}"

        resultado = eval(ecuacion)


print(f"Ecuación: {Ecuacion.ecuacion}")
print(f"Resultado: {Ecuacion.resultado}")

# no se si esta bien, no creo

class Retroalimentacion:
    def revisar_congruencia(self):
        pass

    def retroalimentar(self):
        pass
    # condicional para los colores




