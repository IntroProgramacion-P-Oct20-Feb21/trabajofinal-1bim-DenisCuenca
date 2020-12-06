porcentaje1 = 10
porcentaje2 = 15
porcentaje3 = 20
numeroDias = int(input("Ingrese el número de días hospedados: "))
precioHabitacion = float(input("Ingrese el valor diario de la habitación: "))
subtotal = numeroDias * precioHabitacion
if (numeroDias>5) and (numeroDias<=10):
	descuento = (porcentaje1*subtotal)/100
	valorTotal = subtotal - descuento
else:
	if (numeroDias>5) and (numeroDias<=10):
	    descuento = (porcentaje2*subtotal)/100
	    valorTotal = subtotal - descuento
	else:
		if (numeroDias>5) and (numeroDias<=10):
			descuento =(porcentaje3*subtotal)/100
			valorTotal=subtotal-descuento
		else:
			descuento = 0
			valorTotal = subtotal - descuento
print("El valor subtotal a pagar es: %.2f\nEl descuento es: %2.f\n"
	"El valor total a pagar es: "
	"%.2f\n"%(subtotal,descuento,valorTotal))
