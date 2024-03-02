print("Bienvenidos a la calculador")
print("Para salir escribe salir")
print("Las operaciones son suma, multi, div, resta")

resultado = ""
while True:
    if not resultado:
        resultado = input(f"Ingrese numero: ")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)
    operador = input("Ingresa operación: ")
    if operador.lower() == "salir":
        break
    n2 = input("Ingrese el siguiente número: ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)
    if operador.lower() == "suma":
        resultado += n2
    elif operador.lower() == "resta":
        resultado -= n2
    elif operador.lower() == "multi":
        resultado *= n2
    elif operador.lower() == "div":
        resultado /= n2
    else:
        print("Operación no valida")
        break
    print(f"El resultado es {resultado}")
