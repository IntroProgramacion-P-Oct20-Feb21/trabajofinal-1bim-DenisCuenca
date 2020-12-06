cadenaFinal = ""
bandera = True
res = 0
con = 0
while bandera :
	nota = float(input("Ingrese calificaciones: "))
	res += nota
	con += 1
	cadenaFinal = ("%s%.2f\n"%(cadenaFinal,nota))
	salida = input("Ingrese (s) si desea salir del ciclo: ")
	if salida == "s":
		bandera = False
res /= con
print("Listado de notas\n%s\nY el promedio es: %.2f\n"%(cadenaFinal,res))		
