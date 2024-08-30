#Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro
#correo electronico con el mismo nombre(la parte delante de la arroba @) pero con dominio ceu.es.

correo = input("Ingrese su correo electronico: ")

print(correo[:correo.find("@")]+"@ceu.es.")