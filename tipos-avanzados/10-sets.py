# set grupo o conjunto

primer = {1 ,1 ,2, 2, 3, 4}
segundo = [3, 4 , 5]
segundo = set(segundo)
# primer.add(5)
# primer.remove(1)

print(primer | segundo) #Union
print(primer & segundo) #interseccion
print(primer - segundo) #diferencia
print(primer ^ segundo) #diferencia simetrica
