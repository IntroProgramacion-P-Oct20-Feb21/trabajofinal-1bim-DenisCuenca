precioBase = 0
totalPagar = 0
netflix = 10
disneyPlus = 6
appleTv = 4
amazonPrime = 4.50
impuesto = 0
nombre = input("Ingrese el nombre del usuario: ")
empresa = input("Ingrese el servicio que desea cancelar:"
	"\n1. Netflix\n"
	"2. Disney Plus\n"
	"3. Apple TV\n"
	"4. Amazon Prime\n")
numeroMensualidades = int(input("Ingrese el número de mensualidades a pagar: "))
if empresa == "Netflix" :
	inNetflix = 10
	precioBase = numeroMensualidades * netflix
	impuesto = (precioBase * inNetflix)/100
	totalPagar = precioBase + impuesto
else:
	if empresa == "Disney Plus" :
		inDisneyPlus = 12
		precioBase = numeroMensualidades * disneyPlus
		impuesto = (precioBase * inDisneyPlus)/100
		totalPagar = precioBase + impuesto
	else:
		if empresa == "Amazon Prime" :
			inAmazonPrime = 16
			precioBase = numeroMensualidades * amazonPrime
			impuesto = (precioBase * inAmazonPrime)/100
			totalPagar = precioBase +  impuesto
		else:
			if empresa == "Apple TV":
				inAppleTv = 14
				precioBase = numeroMensualidades * appleTv
				impuesto = (precioBase*inAppleTv)/100
				totalPagar = precioBase + impuesto
			else:
				print("Valor fuera de rango")

print("Usuario: %s\nEmpresa: %s\nPrecio base: $%s\nImpuesto: $%s\nTotal a cancelar: $%s\n"
	%(nombre,empresa,precioBase,impuesto,totalPagar))