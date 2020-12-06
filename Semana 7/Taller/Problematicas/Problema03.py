aumento = 3
numero = 2
cadena = ""
while numero <= 37:
	cadena=("%s%d "%(cadena,numero))
	numero += aumento
	aumento += 2
print(cadena)	
