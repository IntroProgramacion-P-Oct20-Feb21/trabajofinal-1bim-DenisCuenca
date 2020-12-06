cadenaReporte = ""
bandera = True
sumaEdades = 0
SumaEstaturas = 0
contadorIteraciones = 0
cadenaReporte = ("%s%s\n"%(cadenaReporte,"Listado de jugadores:"))
while bandera:
	nombreJugador = input("Ingrese el nombre del jugador: ")
	posicionCampo = input("Ingrese la posición en el campo: ")
	edad = int(input("Ingrese la edad del jugador: "))
	estatura = float(input("Ingrese la estatura del jugador: "))
	sumaEdades = sumaEdades + edad
	SumaEstaturas = SumaEstaturas + estatura
	contadorIteraciones = contadorIteraciones + 1
	cadenaReporte = ("%s%d. %s -%s-, edad %d, estatura %.2f\n"
		%(cadenaReporte,
			contadorIteraciones,
			nombreJugador,
			posicionCampo,
			edad,
			estatura))
	salida = input("Desea salir del ciclo; digite: si")
	if salida == "si":
		bandera = False
promedioEdad = sumaEdades / contadorIteraciones
promedioEstatura = SumaEstaturas / contadorIteraciones
cadenaReporte = ("%sPromedio de edades: %s\nPromedio de estaturas: %.2f\n"%(cadenaReporte,promedioEdad,promedioEstatura))
print("%s\n"%(cadenaReporte))	

