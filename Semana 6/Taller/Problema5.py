contador = 1
cadenaFinal = ""
while contador <=4:
	nombre = input("Ingrese el nombre del estudiante: ")
	promedio = float(input("Ingrese el promedio del estudiante: "))
	if promedio > 7 :
		resultado = "Aprobado"
		cadenaFinal = ("%s%s\t%s\t%s\n"%(cadenaFinal,nombre,promedio,resultado))
	else:
		resultado = "Reprobado"
		cadenaFinal = ("%s%s\t%s\t%s\n"%(cadenaFinal,nombre,promedio,resultado))
	contador += 1
print(cadenaFinal)