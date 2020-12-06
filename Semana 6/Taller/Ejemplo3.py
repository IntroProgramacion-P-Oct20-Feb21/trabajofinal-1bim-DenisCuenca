cadenaFinal = ""
contador = 1
tipoOperación = input("Ingrese el tipo de operación que quiere realizar\nSuma\no\nMultiplicación\n")
numeroTabla = int(input("Ingrese el número de tabla"))
limiteTabla =int(input("Ingrese el limite de la tabla"))
if tipoOperación == "suma":
	cadenaFinal = ("%s%s\n"%(cadenaFinal,"Tabla de sumar"))
	while contador <= limiteTabla:
		operacion  = numeroTabla + contador
		cadenaFinal = ("%s%d + %d = %d\n"%(cadenaFinal, numeroTabla, contador,operacion))
		contador = contador + 1
else:
	if tipoOperación == "multiplicacion":
		cadenaFinal = ("%s%s\n"%(cadenaFinal,"Tabla de multiplicar"))
		while contador <= limiteTabla:
			operacion = numeroTabla * contador 
			cadenaFinal = ("%s%d * %d = %d\n"%(cadenaFinal,numeroTabla,contador,operacion))
			contador += 1
	else:
		cadenaFinal = ("%s%s\n"%(cadenaFinal,"Error en el tipo de operación"))
print(cadenaFinal)
		


