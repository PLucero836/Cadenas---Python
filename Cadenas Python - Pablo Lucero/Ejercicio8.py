#Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre
#por pantalla el numero de euros y el numero de centimos del precio introducido 

precio = input("Introduzca el precio: ")

print("Euros: ", precio[:precio.find(".")], "centimos: ", precio[precio.find(".")+1:])