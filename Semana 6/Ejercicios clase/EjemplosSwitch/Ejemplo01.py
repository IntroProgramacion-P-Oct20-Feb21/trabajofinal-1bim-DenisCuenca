valor1 = int(input("Ingrese el primer valor de la operación: "))
valor2 = int(input("Ingrese el segundo valor de la operación: "))
resultado = 0
op = int(input("Selecione la operación que desea realizar"
	"\nIngrese 1 para sumar\nIngrese 2 para restar\n"
	"Ingrese 3 para multiplicar\n"))
if op == 1:
	resultado = valor1 + valor2
else:
	if op == 2:
		resultado = valor1 - valor2
	else:
		if op == 3:
			resultado = valor1 * valor2
		else:
			print("Operación incorrecta")
print("El resultado de la operación es : %d\n"%(resultado))			