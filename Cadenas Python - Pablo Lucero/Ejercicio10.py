#Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, y 
# muestre por pantalla cada uno de los productos en una linea distinta.

cesta = input("Ingrese los productos separados por comas:\n")

print(cesta.replace(",","\n"))

