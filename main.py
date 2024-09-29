from contact import *

while True:
    print("Contactos")
    print("1. Ingresar un nuevo contacto")
    print("2. Lista de contactos")
    print("3. Buscar un contacto")
    print("4. Salir")

    menu = int(input("Ingrese una opcion: "))

    if menu == 1:
        add_contact()
    elif menu == 2:
        print_contact_list()
    elif menu == 3:
        search_contact()
    elif menu == 4:
        print("Saliendo del programa...")
        break
    else:
        print("Intentelo de nuevo!")