Proceso PiedraPapelTijera
	
	Definir jugador, computadora Como Entero
	Definir opcionJugador, opcionPC Como Cadena
	
	Escribir "=== PIEDRA, PAPEL O TIJERA ==="
	Escribir "1. Piedra"
	Escribir "2. Papel"
	Escribir "3. Tijera"
	Escribir "Seleccione una opción:"
	Leer jugador
	
	computadora <- Aleatorio(1,3)
	
	Segun jugador Hacer
		1:
			opcionJugador <- "Piedra"
		2:
			opcionJugador <- "Papel"
		3:
			opcionJugador <- "Tijera"
		De Otro Modo:
			opcionJugador <- "Opción inválida"
	FinSegun
	
	Segun computadora Hacer
		1:
			opcionPC <- "Piedra"
		2:
			opcionPC <- "Papel"
		3:
			opcionPC <- "Tijera"
	FinSegun
	
	Escribir "Tú elegiste: ", opcionJugador
	Escribir "La computadora eligió: ", opcionPC
	
	Si jugador < 1 O jugador > 3 Entonces
		Escribir "Ingresaste una opción incorrecta"
	Sino
		Si jugador = computadora Entonces
			Escribir "Resultado: Empate"
		Sino
			Si (jugador = 1 Y computadora = 3) O (jugador = 2 Y computadora = 1) O (jugador = 3 Y computadora = 2) Entonces
				Escribir "Resultado: ¡Ganaste!"
			Sino
				Escribir "Resultado: Perdiste"
			FinSi
		FinSi
	FinSi
	
FinProceso