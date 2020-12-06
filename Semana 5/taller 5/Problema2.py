cantidad = int(input("Ingrese la cantidad del árticulo " 
"solicitado en unidades: "))
precio = float(input("Ingrese el valor unitario del árticulo: "))
total = cantidad * precio
if cantidad > 50 :
	descuento = (cantidad * 15)/100
	total -= descuento
print("El valor a pagar es: %.2f"%(total))	