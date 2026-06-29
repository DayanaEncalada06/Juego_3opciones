import random
import time

def pausa():
    input("\nPresiona ENTER para comenzar...")

def menu():
    print("\n=========================================")
    print("       JUEGO PIEDRA PAPEL O TIJERA")
    print("      ESTUDIANTE: DAYANA ENCALADA")
    print("      MATERIA: LOGICA DE PROGRAMACIÓN")
    print("=========================================")
    print("1. Jugar contra la computadora")
    print("2. Jugar contra otro jugador")
    print("3. Salir")
    return input("Seleccione una opción: ")

def despedida():
    print("\n=========================================")
    print("Gracias por jugar Piedra, Papel o Tijera.")
    print("Fue un gusto jugar contigo.")
    print("¡Hasta la próxima!")
    print("=========================================")

def elegir_opcion(nombre):
    while True:
        print(f"\nTurno de {nombre}")
        print("1. Piedra")
        print("2. Papel")
        print("3. Tijera")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            return "Piedra"
        elif opcion == "2":
            return "Papel"
        elif opcion == "3":
            return "Tijera"
        else:
            print("Opción incorrecta. Ingresa 1, 2 o 3.")

def determinar_ganador(opcion1, opcion2):
    if opcion1 == opcion2:
        return "Empate"
    elif (opcion1 == "Piedra" and opcion2 == "Tijera") or \
         (opcion1 == "Papel" and opcion2 == "Piedra") or \
         (opcion1 == "Tijera" and opcion2 == "Papel"):
        return "Jugador1"
    else:
        return "Jugador2"

def contador():
    print("\nPreparados...")
    time.sleep(1)
    print("Piedra...")
    time.sleep(1)
    print("Papel...")
    time.sleep(1)
    print("Tijera...")
    time.sleep(1)
    print("¡YA!")

def mostrar_marcador(nombre1, nombre2, puntos1, puntos2, empates):
    print("\n==============================")
    print("          MARCADOR")
    print("==============================")
    print(f"{nombre1}: {puntos1}")
    print(f"{nombre2}: {puntos2}")
    print(f"Empates: {empates}")

def mostrar_historial(historial):
    print("\n==============================")
    print("     HISTORIAL DE RONDAS")
    print("==============================")

    for ronda in historial:
        print(f"\nRonda {ronda['ronda']}")
        print(f"{ronda['jugador1']} eligió: {ronda['opcion1']}")
        print(f"{ronda['jugador2']} eligió: {ronda['opcion2']}")
        print(f"Resultado: {ronda['resultado']}")

def jugar_partida(modo):
    nombre1 = input("\nIngrese el nombre del jugador 1: ")

    if modo == "1":
        nombre2 = "Computadora"
    else:
        nombre2 = input("Ingrese el nombre del jugador 2: ")

    puntos1 = 0
    puntos2 = 0
    empates = 0
    ronda = 1
    intentos = 3
    historial = []

    while ronda <= intentos:
        print("\n====================================")
        print(f"              RONDA {ronda}")
        print("====================================")

        opcion1 = elegir_opcion(nombre1)

        if modo == "1":
            opcion2 = random.choice(["Piedra", "Papel", "Tijera"])
        else:
            opcion2 = elegir_opcion(nombre2)

        contador()

        print(f"\n{nombre1} eligió: {opcion1}")
        print(f"{nombre2} eligió: {opcion2}")

        resultado = determinar_ganador(opcion1, opcion2)

        if resultado == "Empate":
            print("Resultado: Empate")
            empates += 1
            resultado_texto = "Empate"
        elif resultado == "Jugador1":
            print(f"Resultado: Ganó {nombre1}")
            puntos1 += 1
            resultado_texto = f"Ganó {nombre1}"
        else:
            print(f"Resultado: Ganó {nombre2}")
            puntos2 += 1
            resultado_texto = f"Ganó {nombre2}"

        historial.append({
            "ronda": ronda,
            "jugador1": nombre1,
            "jugador2": nombre2,
            "opcion1": opcion1,
            "opcion2": opcion2,
            "resultado": resultado_texto
        })

        mostrar_marcador(nombre1, nombre2, puntos1, puntos2, empates)

        ronda += 1

        if ronda > intentos and puntos1 == puntos2:
            print("\nHay empate en el marcador.")
            print("Se agrega una ronda extra de desempate.")
            intentos += 1

    print("\n=========================================")
    print("             RESULTADO FINAL")
    print("=========================================")
    print(f"{nombre1}: {puntos1}")
    print(f"{nombre2}: {puntos2}")
    print(f"Empates: {empates}")

    if puntos1 > puntos2:
        ganador = nombre1
    else:
        ganador = nombre2

    print("\n🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆")
    print("    GANADOR")
    print(f"    {ganador.upper()}")
    print("🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆")

    mostrar_historial(historial)

def preguntar_reinicio():
    print("\n=========================================")
    print("¿Desea jugar nuevamente?")
    print("1. Sí")
    print("2. No")
    opcion = input("Seleccione una opción: ")

    while opcion != "1" and opcion != "2":
        print("Opción incorrecta. Ingrese 1 o 2.")
        opcion = input("Seleccione una opción: ")

    return opcion

def juego():
    pausa()

    while True:
        opcion = menu()

        if opcion == "1":
            jugar_partida("1")
            reiniciar = preguntar_reinicio()
            if reiniciar == "2":
                despedida()
                break

        elif opcion == "2":
            jugar_partida("2")
            reiniciar = preguntar_reinicio()
            if reiniciar == "2":
                despedida()
                break

        elif opcion == "3":
            print("\nElegiste salir del juego.")
            despedida()
            break

        else:
            print("Opción incorrecta. Ingrese 1, 2 o 3.")

juego()