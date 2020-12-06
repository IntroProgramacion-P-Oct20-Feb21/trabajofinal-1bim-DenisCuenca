bandera = True
cadenaFinal =""
while bandera :
	nombre = input("Ingrese el nombre del empleado: ")
	numeroDias = int(input("Ingrese el número de días trabajados: "))
	costoDia = float(input("Ingrese el costo del día de trabajo: "))
	sueldo = numeroDias * costoDia
	cadenaFinal = ("%s%s\t%s\t$%s\t$%.2f\n"%(cadenaFinal,nombre,numeroDias,costoDia,sueldo))
	n1 = input("Escriba 'no' para salir del bucle: ")
	if n1 == "no" :
		bandera = False
print(cadenaFinal)		