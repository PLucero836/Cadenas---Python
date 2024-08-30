#Los telefonos de una empresa tienen el siguiente formato prefijo-numero-extension- donde el prefijo es el codigo
#del pais +34 y la extension tiene dos digitos(por ejemplo +34-913724710-56). Escribir un programa que pregunta por 
#un numero de telefono  con este formato y muestre por pantalla el numero de telefono sin el prefijo y la extension

numero = input("Escriba un numero de telefono con el formato +xx-xxxxxxxxx-xx:")
print("El numero es", numero[4:-3])

