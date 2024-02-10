"""RETO 4 DE DIA JUEVES de Alfredo Ruiz"""

import sys

def opcion_A():
    print('"la cantidad maximas de usuarios a gregar es de 5"')

    intentos = 3
    for intentos in range(0, 3):
        try:
            max_usuarios = int ( input("Ingrese la cantidad de usuarios a registrar: "))
            if 1 <= max_usuarios <=5:
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

        usuarios_registrados = {}

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
                    Telefono = input("Agrege su Numero Telefonico: ").isdigit()

                    caract_telefono = len(Telefono)
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

            usuarios_registrados = {Nombre, Apellido, Telefono, Correo}
            print(f'"{max_usuarios} Usuarios registrados:"')
            print('"Felicidades sean Biemvenidos"')


global nuevos_registrados
nuevos_registrados = opcion_A




def opcion_B(usuarios_lista):
        for i, (nombre, apellido, telefono, correo) in enumerate(usuarios_lista):
            nombre_completo = f"{nombre} {apellido}"
            print(f"{i}. Nombre: {nombre_completo}, Telefono: {telefono}, Correo: {correo}")



def opcion_C():
    intentos = 3
    while intentos >=0:
        indice = int(input("Indice del usuario a actualizar: "))
        if 0 <= indice < len(list(nuevos_registrados.keys() ) ):
            usuario = nuevos_registrados.get(indice, "Usuario no encontrado")
            if usuario is not None:
                print(f"Actualizando datos para: Nombre: {usuario['nombre']}, Telefono: {usuario.telefono}, Correo: {usuario.correo}")
                opcion_A()
            else:
                print(f"El indice {indice} no corresponde a ningun usuario registrado.")
                break
        else:
            print("El indice debe ser un numero entre 0 y {len(usuarios_registrados) - 1}")

def opcion_D():
    pass

def main():

    intentos = 3
    while intentos >=0:

        print('"Escoja una opcion"')
        print("Opcion A para registrar nuevos usuarios")
        print("Opcion B para ver la lista de usuarios")
        print("Opcion C para editar usuarios")
        print("Opcion D para borar algun usario")
        print("Si desea salir del programa presione S")

        Alternativa = str(input("Opcion: ")).upper()
        print("tu opcion fue", Alternativa)
        break
    if Alternativa in funciones.keys():
        funcion_nombre = f"opcion_{Alternativa}"
        funcion = getattr(sys.modules[__name__], funcion_nombre)
        funcion()

    else:
        print("lo siento, no se ha ingresado una opcion valida, hasta luego!")
        sys.exit()

funciones = {
        "A": opcion_A,
        "B": opcion_B,
        "C": opcion_C,
        "D": opcion_D,
        }

if __name__== "__main__":
    main()
