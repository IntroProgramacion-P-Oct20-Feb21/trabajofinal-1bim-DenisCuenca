#Solución que permita calcular y mostrar el valor a cancelar de 
#una planilla de luz. Se debe ingresar el valor de costo por 
#kilovatio/hora y el número de kilovatios consumidos en el mes. 
#Si el usuario tiene edad mayor a 65 años, se debe descontrar el 10%.
#

costoHora = float(input("Ingrese el costo de kilovatios consumidos por hora: "))
kilMes = float(input("Ingrese el número de kilovatios consumidos en el mes: "))
edad = int(input("Ingrese su edad: "))

kilHora = kilMes * 720 
total = costoHora * kilHora
if edad >= 65:	
	descuento = (total * 10)/100
	total -= descuento
print("El valor a pagar es: %.2f"%(total))	
