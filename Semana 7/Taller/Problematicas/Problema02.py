# 2 6 12 20 30 42 56 72 90 110
aumento = 4
numero = 2
cadena = ""
while numero <= 110:
	cadena = ("%s%d "%(cadena,numero))
	numero = numero + aumento
	aumento += 2
print(cadena)	
