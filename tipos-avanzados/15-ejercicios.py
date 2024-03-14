from pprint import pprint

cadena1 = "Ejercios de prueba de tipos avanzados"
cadena2 = "mensajes"


def delSpace(cadena):
    return [char for char in cadena if char != " "]


print(delSpace(cadena1))


def countChar(lista):
    chars_dict = {}
    for char in lista:
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    return chars_dict


contados = countChar(cadena2)
pprint(contados, width=1)


def orderBy(diccionario):
    return sorted(
        diccionario.items(),
        key=lambda key: key[1],
        reverse=True
    )


ordenados = orderBy(contados)
print(ordenados)


def mayores_tuplas(lista):
    maximo = lista[0][1]
    respuesta = {}
    for orden in lista:
        if maximo > orden[1]:
            break
        respuesta[orden[0]] = orden[1]
    return respuesta


mayores = mayores_tuplas(ordenados)
print(mayores)


def crea_mensaje(diccionario):
    message = "Los que más se repiten son: \n"
    for key, valor in diccionario.items():
        message += f"- {key} con {valor} repeticiones \n"
    return message


mensaje = crea_mensaje(mayores)
print(mensaje)
