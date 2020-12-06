nombre=input("Ingrese el nombre de una ciudad del Ecuador")
valor = nombre[0]
if valor == 'a' or valor == 'A':
	print("Nombre con inicial %s de %s\n"%(valor,nombre.lower()))
else:
	if valor == 'e' or valor == 'E':
		print("Nombre con inicial %s de %s\n"%(valor,nombre.lower()))
	else:
		if valor == 'i' or valor == 'I':
			print("Nombre con inicial %s de %s\n"%(valor,nombre.lower()))
		else:
			if valor == 'o' or valor == 'O':
				print("Nombre con inicial %s de %s\n"%(valor,nombre.lower()))
			else:
				print("Opción incorrecta; noguna de las anteriores")