marca = input("Ingrese la marca del automóvil: ")
costo = float(input("Ingrese el origen de su automóvil")
origen = int(input("Ingrese el origen del automóvil:\n1. Alemania\n2. Japón\n3. Italia\n4. USA")
if origen == 1:
	descuento = (costo * 20)/100;
	costo -= descuento
else:
	if origen == 2:
		descuento = (costo * 30)/100
	    costo -= descuento
    else:
    	if origen == 3:
		    descuento = (costo * 15)/100
	        costo -= descuento
        else:
      		if origen == 4:
	        	descuento = (costo * 8)/100
	            costo -= descuento
            else:
            	print ("Fuera de rango")8
print("Datos del automóvil %s :\nDescuento: %.2f\nPrecio final: %.2f\n"%(marca,descuento,costo))