#Escribir un programa que pregunte el nombre del usuario en la consola y despues de que el usuario lo introduzca
#muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre del usuario en mayusculas y <n> es 
#el numero de letras que tiene el nombre

nombre = input("Escriba su nombre completo")

print(nombre.upper()+" tiene "+str(len(nombre))+" letras")
