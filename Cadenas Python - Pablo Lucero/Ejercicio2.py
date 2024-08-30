#Escriba un programa que pregunte el nombre del usuario en la consola y despues muestre por pantalla el nombre
#completo del usuario tres veces, una con todas las letras minusculas, otra con todas las letras mayusculas y otra
# solo con la primera letra del nombre y de los apedillos en mayusculas. El usuario puede introducir su nombre 
# combinado mayuscula y minusculas como quiera

nombre = input("Introduce tu nombre completo: ")

print(nombre.lower())
print(nombre.upper())
print(nombre.title())
