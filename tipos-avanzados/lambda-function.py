# function lambda
def lambda_cube(x): return x*x*x


print(lambda_cube(15))
# result 3375

# function map
fruit = ["apple", "grapes", "orange", "cherry", "kiwi"]

result = map(lambda x: x.title(), fruit)

for data in result:
    print(data, end=' ')
# result Apple Grapes Orange Cherry Kiwi


# function filter
fruit = ["apple", "grapes", "orange", "cherry", "kiwi"]

# using filter function
result = filter(lambda x: len(x) < 5, fruit)

for data in result:
    print(f"\n{data}")
# result kiwi


# function Zip
fruit = ["apple", "grapes", "orange", "cherry", "kiwi"]
price = [100, 80, 40, 60]

result = zip(f"{fruit}\n", price)

for info in result:
    print(info, end='')
# result ('apple', 100)('grapes', 80)('orange', 40)('cherry', 60)

# function enumerate
fruit = ["apple", "grapes", "orange", "cherry", "kiwi"]

# traditional iterable
for i in range(len(fruit)):
    print(i, fruit[i])

# using enumerate function
for idx, name in enumerate(fruit):
    print(f"{idx}", name)
