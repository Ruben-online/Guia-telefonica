class Contact:
    def __init__(self, name, number, nick_name):
        self.name = name
        self.number = number
        self.nick_name = nick_name

    def __str__(self):
        return f"Nombre: {self.name}\nNúmero: {self.number}\nApodo: {self.nick_name}\n"


contact_list = []


def add_contact():
    name = input("Ingrese el nombre: ")
    number = input("Ingrese el número: ")
    nick_name = input("Ingrese el apodo: ")

    new_contact = Contact(name, number, nick_name)
    contact_list.append(new_contact)
    print("\nContacto agregado exitosamente\n")


def print_contact_list():
    if not contact_list:
        print("No hay contactos guardados")
        return

    print("Contactos guardados")
    for contact in contact_list:
        print(contact)
    print()


def search_contact():
    search = input("Que contacto desea buscar?: ")

    found = False
    for contact in contact_list:
        if contact.name == search:
            print(f"El contacto {search} si esta en la lista")
            found = True
            break
        elif contact.number == search:
            print(f"El contacto con el numero {search} si esta en la lista")
            found = True
            break
        elif contact.nick_name == search:
            print(f"El contacto con el apodo {search} si esta en la lista")
            found = True
            break

    if not found:
        print(f"No se encontro el contacto")
