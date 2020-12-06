contador = 1
num = 1
den = 3
cadena = "1"
resultado = 1
while den <= 15:
	if (contador % 2) == 0:
		cadena = ("%s+%d/%d"%(cadena,num,den))
		den += 2
		contador += 1
		resultado += num/den 
	else:
		cadena = ("%s-%d/%d"%(cadena,num,den))
		den += 2
		contador += 1
		resultado -= num/den
cadena = ("%s\nResultado: %.2f\n"%(cadena,resultado))		
print(cadena)		
