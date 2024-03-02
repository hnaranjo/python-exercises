cadena = input("Ingrese la palabra o frase: ")


def es_palindromo(text):
    text1 = changeString(text)
    text2 = changeString(text[::-1])
    res = True if text1 == text2 else False
    return res


def changeString(text):
    newText = text.lower().replace(' ', '')
    return newText


print(cadena, es_palindromo(cadena))
