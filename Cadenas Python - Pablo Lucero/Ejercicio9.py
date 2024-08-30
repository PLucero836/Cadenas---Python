#Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestre por pantalla,
#el dia, el mes y el año. Adaptar el programa anterior para que tambien funcione cuando el dia o el mes se introduzcan
#con un solo caracter.

fecha = input("Ingrese su fecha de nacimiento\n")

dia=fecha[:fecha.find("/")]
mesaño=fecha[fecha.find("/")+1:]

mes=mesaño[:mesaño.find("/")]
año=mesaño[mesaño.find("/")+1:]

print(dia)
print(mes)
print(año)

