def hola():
    print("Hola mundo")
    print("Ultimate Python")


def holaName(name, lastName="Prueba"):
    print(f"Hola {name} {lastName}")


hola()
holaName("Hector", "Naranjo")
holaName("Mensaje")
holaName(lastName="Naranjo", name="Hector")
