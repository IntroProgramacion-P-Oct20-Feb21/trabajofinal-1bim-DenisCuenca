limite = 3
contador = 1
suma_total = 0
print("Ingrese las notas de los estudiantes de su materia")
while contador <= limite:
	calificacion = float(input("Ingrese calificaciones número %d"%(contador)))
	suma_total = suma_total + calificacion
	contador = contador + 1
promedio_final = suma_total/limite
print("El promedio final es: %.2f\n"%(promedio_final))