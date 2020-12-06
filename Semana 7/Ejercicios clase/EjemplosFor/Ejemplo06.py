tabla = int(input("Ingrese el número de la tabla generar: "))
for contador in range (5,31):
	operacion = tabla * contador
	print("%d x %d = %d\n"%(tabla,contador,operacion))