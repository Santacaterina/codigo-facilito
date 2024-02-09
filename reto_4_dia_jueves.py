"""RETO 4 DE DIA JUEVES de Alfredo Ruiz"""

import sys

intentos = 3
while intentos >=0:

    print('"Escoja una opcion"')
    print("Opcion A para registrar nuevos usuarios")
    print("Opcion B para ver la lista de usuarios")
    print("Opcion C para editar usuarios")
    print("Si desea salir del programa presione S")
    
    Opcion = input("Opcion: ").upper()

#Para la opcion A
    
    if Opcion == "A":
#datosa
        
        print('"la cantidad maximas de usuarios a gregar es de 5"')

        intentos = 3
        while intentos >=0:
            try:
                max_usuarios = int ( input("Ingrese la cantidad de usuarios a registrar: "))
                if 1<= max_usuarios <=5:
                    break
                else:
                    intentos -= 1
                    if intentos > 0:
                        print(f"vuelva a escribir la cantidad de usuarios, le quedan {intentos} intentos mas")
                        print('" Recuerde que la cantidad maximas de usuarios a gregar es de 5"')
                    else:
                        print("lo siento, no se ha ingresado una cantidad valida, hasta luego!")
                        sys.exit()
            except ValueError:
                intentos -= 1
                if intentos > 0:
                    print("Por favor, ingrese un numero entero Valido.")
                    print(f"vuelva a escribir la cantidad de usuarios, le quedan {intentos} intentos mas")

        print('"el Nombre, Apellido, correo deben de tener una longitud minima de 5 y un maximo de 50 caracteres"')

        usuarios_registrados = []

        #Nombre
        for i in range(max_usuarios):
            print(f"Ingrese el usuario Nº {i+1}")
            intentos = 3
            while intentos >=0: 
                Nombre = input("Agrege su Primer Nombre: ")
                caract_nombre = len(Nombre)
                if 5 <= caract_nombre <= 50:
                    break
                else:
                    intentos -= 1
                    if intentos > 0:
                        print(f"vuelva a escribir su nombre, le quedan {intentos} intentos mas")
                        print("Recuede que debe ingresar un Nombre con una longitud minima de 5 y un maximo de 50 caracteres")
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
                        print(f"vuelva a escribir su apellido, le quedan {intentos} intentos mas")
                        print("Recuede que debe ingresar un Apellido con una longitud minima de 5 y un maximo de 50 caracteres")
                    else:
                        print("lo siento, no se ha ingresado un apellido valido, hasta luego!")
                        sys.exit()

            #telefono
            intentos = 3
            print("debe ingresar un numero telefonico de 10 caracteres pero omitiendo el primer 0 si es el caso")
            while intentos >=0:
                try:
                    Telefono = int(input("Agrege su Numero Telefonico: ")) 

                    caract_telefono = len(str(Telefono))
                    if caract_telefono == 10:
                        break
                    else:
                        intentos -= 1
                        if intentos > 0:
                            print(f"vuelva a escribir su Numero Telefono, le quedan {intentos} intos mas")
                            print("Recuede que debe ingresar un numero telefonico de 10 caracteres")
                        else:
                            print("lo siento, no se ha ingresado un Telefono valido, hasta luego!")
                            sys.exit()
                except ValueError:
                    print(f"vuelva a escribir su Numero Telefono, le quedan {intentos} intos mas")
                    print("Recuede que debe ingresar un numero telefonico de 10 caracteres")

            #correo
            Correo = input("Agrege su Correo Electronico: ")

            usuarios_registrados.append((Nombre, Apellido, Telefono, Correo))

        print(f'"{max_usuarios} Usuarios registrados:"')
        print('"Felicidades sean Biemvenidos"')


    elif Opcion == "B":
        for i, usuario in enumerate(usuarios_registrados):
            nombre_completo =f"{usuario[0]} {usuario[1]}"
            print(f"{i}. Nombre: {nombre_completo}, Telefono: {usuario[2]}, Correo: {usuario[3]}")

    elif Opcion == "C":
        intentos = 3
        while intentos >=0:
            indice = int(input("Indice del usuario a actualizar: "))
            if 0 <= indice < len(usuarios_registrados):
                usuario = usuarios_registrados [indice]
                print(f"Actualizando datos para: Nombre: {nombre_completo}, Telefono: {usuario[indice]}, Correo: {usuario[indice]}:")

            #Nuevo Nombre
            intentos = 3
            while intentos >=0: 
                Nuevo_Nombre = input("Agrege su Primer Nombre a actualizar: ")
                caract_nombre = len(Nombre)
                if 5 <= caract_nombre <= 50:
                    break
                else:
                    intentos -= 1
                    if intentos > 0:
                        print(f"vuelva a escribir su nombre, le quedan {intentos} intentos mas")
                        print("Recuede que debe ingresar un Nombre con una longitud minima de 5 y un maximo de 50 caracteres")
                    else:
                        print("lo siento, no se ha ingresado un nombre valido, hasta luego!")
                        sys.exit()

            #Nuevo Apellido
            intentos = 3
            while intentos >=0:
                Nuevo_Apellido = input("Agrege su Primer Apellido a actualizar: ")
                caract_apellido = len(Apellido)
                if 5 <= caract_apellido <= 50:
                    break
                else:
                    intentos -= 1
                    if intentos > 0:
                        print(f"vuelva a escribir su apellido, le quedan {intentos} intentos mas")
                        print("Recuede que debe ingresar un Apellido con una longitud minima de 5 y un maximo de 50 caracteres")
                    else:
                        print("lo siento, no se ha ingresado un apellido valido, hasta luego!")
                        sys.exit()

            #Nuevo Telefono
            intentos = 3
            print("debe ingresar un numero telefonico de 10 caracteres pero omitiendo el primer 0 si es el caso")
            while intentos >=0:
                try:
                    Nuevo_Telefono = int(input("Agrege su Numero Telefonico a actualizar: "))

                    caract_telefono = len(str(Telefono))
                    if caract_telefono == 10:
                        break
                    else:
                        intentos -= 1
                        if intentos > 0:
                            print(f"vuelva a escribir su Numero Telefono, le quedan {intentos} intos mas")
                            print("Recuede que debe ingresar un numero telefonico de 10 caracteres")
                        else:
                            print("lo siento, no se ha ingresado un Telefono valido, hasta luego!")
                            sys.exit()
                except ValueError:
                    print(f"vuelva a escribir su Numero Telefono, le quedan {intentos} intos mas")
                    print("Recuede que debe ingresar un numero telefonico de 10 caracteres")

            #Nuevo Correo
            Nuevo_Correo = input("Agrege su Correo Electronico a actualizar: ")

            usuarios_registrados[indice] = (Nuevo_Nombre, Nuevo_Apellido, Nuevo_Telefono, Nuevo_Correo)
            print(usuarios_registrados)
            print("Datos Actualizados Correctamente")
            break
        continue
    
    #para salir del programa
    elif Opcion == "S":
        print('"Hasta Luego"')
        break

    #por si colocan un caracter distinto: a, b, c, s
    else:
        intentos -= 1
        if intentos > 0:
            print(f"vuelva a escribir una opcion valida, le quedan {intentos} intentos mas")
                
        else:
            print("lo siento, no se ha ingresado una opcion valido, hasta luego!")
            sys.exit()





