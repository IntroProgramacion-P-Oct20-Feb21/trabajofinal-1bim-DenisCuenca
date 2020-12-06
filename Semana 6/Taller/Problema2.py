contador = 1
denPar = 20
denImpar = 10
cadenaFinal = ""
while contador <= 6 :
	if (contador % 2)==0 :
		cadenaFinal = ("%s%s/%s "%(cadenaFinal,contador,denPar))
		denPar += 1
	else:
		cadenaFinal = ("%s%s/%s "%(cadenaFinal,contador,denImpar))
		denImpar += 1
	contador += 1
print(cadenaFinal)