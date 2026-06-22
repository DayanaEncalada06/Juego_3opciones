Proceso PiedraPapelTijera
	
	// Variables principales
	Definir jugador, computadora Como Entero
	Definir puntosJugador, puntosComputadora, empates Como Entero
	Definir continuar Como Caracter
	Definir opcionJugador, opcionPC Como Cadena
	
	puntosJugador <- 0
	puntosComputadora <- 0
	empates <- 0
	continuar <- "S"
	
	Escribir "===================================="
	Escribir "      JUEGO: PIEDRA PAPEL TIJERA"
	Escribir "===================================="
	
	// Bucle principal: permite jugar varias veces
	Mientras continuar = "S" O continuar = "s" Hacer
		
		Escribir ""
		Escribir "Seleccione una opción:"
		Escribir "1. Piedra"
		Escribir "2. Papel"
		Escribir "3. Tijera"
		Leer jugador
		
		// Validación de la opción ingresada
		Mientras jugador < 1 O jugador > 3 Hacer
			Escribir "Opción incorrecta. Ingrese 1, 2 o 3:"
			Leer jugador
		FinMientras
		
		// La computadora elige una opción aleatoria
		computadora <- Aleatorio(1,3)
		
		// Convertir número del jugador a texto
		Segun jugador Hacer
			1:
				opcionJugador <- "Piedra"
			2:
				opcionJugador <- "Papel"
			3:
				opcionJugador <- "Tijera"
		FinSegun
		
		// Convertir número de la computadora a texto
		Segun computadora Hacer
			1:
				opcionPC <- "Piedra"
			2:
				opcionPC <- "Papel"
			3:
				opcionPC <- "Tijera"
		FinSegun
		
		Escribir ""
		Escribir "Tú elegiste: ", opcionJugador
		Escribir "La computadora eligió: ", opcionPC
		
		// Condicionales para determinar el ganador
		Si jugador = computadora Entonces
			Escribir "Resultado: Empate"
			empates <- empates + 1
		Sino
			Si (jugador = 1 Y computadora = 3) O (jugador = 2 Y computadora = 1) O (jugador = 3 Y computadora = 2) Entonces
				Escribir "Resultado: ¡Ganaste!"
				puntosJugador <- puntosJugador + 1
			Sino
				Escribir "Resultado: Ganó la computadora"
				puntosComputadora <- puntosComputadora + 1
			FinSi
		FinSi
		
		// Mostrar marcador actual
		Escribir ""
		Escribir "----- MARCADOR -----"
		Escribir "Jugador: ", puntosJugador
		Escribir "Computadora: ", puntosComputadora
		Escribir "Empates: ", empates
		
		// Preguntar si desea jugar otra ronda
		Escribir ""
		Escribir "¿Desea jugar otra vez? S/N"
		Leer continuar
		
	FinMientras
	
	// Resultado final del juego
	Escribir ""
	Escribir "===================================="
	Escribir "          RESULTADO FINAL"
	Escribir "===================================="
	Escribir "Puntos del jugador: ", puntosJugador
	Escribir "Puntos de la computadora: ", puntosComputadora
	Escribir "Empates: ", empates
	
	Si puntosJugador > puntosComputadora Entonces
		Escribir "Ganador final: Jugador"
	Sino
		Si puntosComputadora > puntosJugador Entonces
			Escribir "Ganador final: Computadora"
		Sino
			Escribir "Resultado final: Empate"
		FinSi
	FinSi
	
	Escribir "Gracias por jugar."
	
FinProceso