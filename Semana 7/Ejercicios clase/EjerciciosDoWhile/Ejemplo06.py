contador = 1
tabla = int(input("Ingrese la tabla a generar: "))
while contador <= 10 :
	operacion = tabla * contador
	print("%d x %d = %d\n"%(tabla,contador,operacion))
	contador = contador + 1