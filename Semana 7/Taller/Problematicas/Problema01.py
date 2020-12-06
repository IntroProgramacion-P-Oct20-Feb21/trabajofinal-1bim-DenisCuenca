contador = 1
bandera = True
cadena = ""
sumaEdades = 0
sumaEstaturas = 0
while bandera :
	nombre =  input("Ingrese el nombre del jugador: ")
	posicion = input("Ingrese la posición del jugador: ")
	edad = int(input("Ingrese la edad del jugador: "))
	estatura = float(input("Ingrese la estaura del jugador: "))
	sumaEdades = sumaEdades + edad
	sumaEstaturas = sumaEstaturas + estatura
	cadena = ("%s%d. %s -%s-, edad %d, estatura %.2f\n"%(cadena,contador,nombre,posicion,edad,estatura))
	desicion = input("Escriba 'no' para mostrar el reporte: ")
	desicion = desicion.lower()
	contador += 1
	if desicion == "no":
		bandera = False
promedioEdades = sumaEdades/contador		
promedioEstaturas = sumaEstaturas/contador
cadena = ("%sPromedio de edades: %.2f\nPromedio de estaturas: %.2f\n"
	%(cadena,promedioEdades,promedioEstaturas))
print(cadena)