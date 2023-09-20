
verde = 94, 204, 42
amarillo = 237, 255, 20
gris = 83, 83, 83
gris_claro = 236, 236, 236

from dataclasses import dataclass
import random

@dataclass

class Jugador:
    def registrar_jugador(self):

        nombre_usuario = []
        usuario = input("Ingrese su nombre: ")
        nombre_usuario.append(usuario)

        print("su nombre es:")   # para verificar si funciono
        for elemento in nombre_usuario:
            print(elemento)

        correo_usuario = []
        usuario = input("Ingrese su correo: ")    #si lo vuelvo a hacer con usuario se sobre escribe?
        correo_usuario.append(usuario)

        print("su correo es:")   # para verificar si funciono
        for elemento in correo_usuario:
            print(elemento)



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
        pass

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


    def retroalimentar(self, ecuacion_original: Ecuacion, ecuacion_recibida):

        List = ["", "", "", "", "", "", "", ""]
        color_codigo = [gris_claro, gris_claro, gris_claro, gris_claro, gris_claro, gris_claro, gris_claro, gris_claro]

        for x in range(0, 9):
            if ecuacion_recibida[x] in ecuacion_original:
                color_codigo[x] = amarillo

            if ecuacion_original[x] == ecuacion_recibida[x]:
                color_codigo[x] = verde

        list(ecuacion_recibida)

        for x in range(0, 9):
            List[x] = (ecuacion_recibida[x], True, gris)

        if color_codigo == [verde, verde, verde, verde, verde, verde, verde, verde]:
            return True



