limite_inferior = 10
limite_superio = 20
contador = 10
suma = 0
while (contador>= limite_inferior) and (contador<=limite_superio):
	suma = suma + contador
	print("Contador %d\n"%(contador))
	contador = contador + 1
print("La suma final es %d\n"%(suma))	 