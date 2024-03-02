n1 = input("Ingresa el primer numero: ")
n2 = input("Ingresa el segundo numero: ")
n1 = int(n1)
n2 = int(n2)
suma = n1 + n2
resta = n1 - n2
multi = n1 * n2
div = n1 / n2

mensaje = f"""
Par los númerso {n1} y {n2},
el resutaldo de la suma es {suma},
el resutaldo de la resta es {resta},
el resutaldo de la multiplicación es {multi},
el resutaldo de la división es {div}.
"""
print(mensaje)
