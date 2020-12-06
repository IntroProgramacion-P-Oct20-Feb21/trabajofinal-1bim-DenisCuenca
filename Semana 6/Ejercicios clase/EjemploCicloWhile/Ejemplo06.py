bandera = True
suma_total = 0
print("Ingrese las notas de los estudiantes de su materia")
while bandera:
	calificacion = float(input("Ingrese calificaciones: "))
    suma_total = suma_total + calificacion
    temporal = int(input("Ingrese el valor de -1 para salir del ciclo\n"))
    if temporal == -1:
	    bandera = False
print("Suma de calificaciones es %.2f\n"%(suma_total))
