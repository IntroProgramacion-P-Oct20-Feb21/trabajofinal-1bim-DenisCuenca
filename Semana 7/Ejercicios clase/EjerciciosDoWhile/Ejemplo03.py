cadenaFinal = ""
bandera = True
while bandera :
	nota = float(input("Ingrese calificaciones: "))
	cadenaFinal = ("%s%.2f\n"%(cadenaFinal,nota))
	salida = int(input("Ingrese (-111) si desea salir del ciclo: "))
	if salida == -111 :
		bandera = False
print("Listado de Notas\n%s\n"%(cadenaFinal))	