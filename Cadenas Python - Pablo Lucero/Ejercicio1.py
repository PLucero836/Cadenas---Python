#Escribir un programa que pregunte el nombre del usuario en la consola y un numero entero e imprima
#por pantalla en lineas distintas el nombre del usuario tantas veces como el numero introducido

nombre = input("Escriba un nombre: ");
n=int(input("Escriba un numero: "));

print((nombre+"\n")*n);