#Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal en minuscula, y 
#despues muestre por pantalla la misma frase pero con la vocal introducida en mayuscula

frase = input("INTRODUZCA UNA FRASE \n")
vocal = input("INTRODUZCA UNA VOCAL EN MINUSCULA \n")

print(frase.replace(vocal, vocal.upper()))