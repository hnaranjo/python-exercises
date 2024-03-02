buscar = 10
for numero in range(5):
    print(numero)
    if numero == buscar:
        print("encontrado", buscar)
        break
else:
    print("Elemento no encontrado")


for char in "Ultimate Python":
    print(char)
