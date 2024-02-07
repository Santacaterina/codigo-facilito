"""RETO 1 DE DIA LUNES de Alfredo Ruiz"""

import sys
#datos
print('"la cantidad maximas de usuarios a gregar es de 5"')

intentos = 3
while intentos >=0: 
    max_usuarios = int ( input("Ingrese la cantidad de usuarios a registrar: "))
    if 1<= max_usuarios <=5:
        break
    else:
        intentos -= 1
        if intentos > 0:
            print(f"vuelva a escribir la cantidad de usuarios, le quedan {intentos} intos mas")
            print('" Recuerde que la cantidad maximas de usuarios a gregar es de 5"')
        else:
            print("lo siento, no se ha ingresado una cantidad invalida, hasta luego!")
            sys.exit()

print('"el Nombre, Apellido, correo deben de tener una longitud minima de 5 y un maximo de 50 caracteres"')

usuarios_registrados = []

#Nombre
for i in range(max_usuarios):
    print("ingrese el siguiente usuario")
    intentos = 3
    while intentos >=0: 
        Nombre = input("Agrege su Primer Nombre: ")
        caract_nombre = len(Nombre)
        if 5 <= caract_nombre <= 50:
            break
        else:
            intentos -= 1
            if intentos > 0:
                print(f"vuelva a escribir su nombre, le quedan {intentos} intos mas")
            else:
                print("lo siento, no se ha ingresado un nombre valido, hasta luego!")
                sys.exit()

    #Apellido
    intentos = 3
    while intentos >=0: 
        Apellido = input("Agrege su Primer Apellido: ")
        caract_apellido = len(Apellido)
        if 5 <= caract_apellido <= 50:
            break
        else:
            intentos -= 1
            if intentos > 0:
                print(f"vuelva a escribir su apellido, le quedan {intentos} intos mas")
            else:
                print("lo siento, no se ha ingresado un apellido valido, hasta luego!")
                sys.exit()

    #telefono
    intentos = 3
    print("debe ingresar un numero telefonico de 10 caracteres")
    while intentos >=0: 
        Telefono = input("Agrege su Numero Telefonico: ")
        caract_telefono = len(Telefono)
        if 0 != caract_telefono == 10:
            break
        else:
            intentos -= 1
            if intentos > 0:
                print(f"vuelva a escribir su Numero Telefono, le quedan {intentos} intos mas")
                print("Recuede que debe ingresar un numero telefonico de 10 caracteres")
            else:
                print("lo siento, no se ha ingresado un Telefono valido, hasta luego!")
                sys.exit()

    #correo
    Correo = input("Agrege su Correo Electronico: ")

    usuarios_registrados.append((Nombre, Apellido, Telefono, Correo))
print("Usuarios registrados")
for usuario in usuarios_registrados:
    print(f"Nombre: {usuario[0]}, Apellido: {usuario[1]}, Telefono: {usuario[2]}, Correo: {usuario[3]}")
#mensaje de respuesta 
print("Biemvenidos")