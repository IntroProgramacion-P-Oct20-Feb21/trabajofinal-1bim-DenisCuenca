contador = 1
cadena = ""
while contador <= 5:
	cadena = ("%sTabla de multiplicar ddel número: %d\n"%(cadena,contador))
	for i in range(1,11):
		operacion = i*contador
		cadena = ("%s%d x %d = %d\n"%(cadena,contador,i,operacion))
	print("\n")
	cadena = ("%s\n"%(cadena))
	contador += 1
print("%s\n"%(cadena))		