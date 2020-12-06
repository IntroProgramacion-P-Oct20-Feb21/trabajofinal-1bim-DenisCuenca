contador = 1
cadenaFinal = ""
while contador <= 10 :
	nombre = input("Ingrese el nombre del jugador: ")
	puntos = int(input("Ingrese la cantidad de puntos anotados por el jugador: "))
	faltas = int(input("Ingrese la cántidad de faltas cometidas por el jugador: "))
	cadenaFinal = ("%s%s\t%s\t%s\n"%(cadenaFinal,nombre,puntos,faltas))
	contador += 1
print(cadenaFinal)	 