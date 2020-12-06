monto = float(input("Ingrese el monto total de su prestamo: "))
interes = float(input("Ingrese inerés mensual a cobrar: "))
montoMes = monto / 12
total = montoMes + interes
round(total)
print("%.2f"%(total))
