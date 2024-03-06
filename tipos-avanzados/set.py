# creating a set
fruits = {'apple', 'banana', 'orange'}
print(fruits)

# Adding to a set
fruits.add('grape')
print(fruits)


# Removing from a set
fruits.remove('banana')
print(fruits)


set_A = {1, 2, 3}
set_B = {3, 4, 5}

union_set = set_A | set_B
intersection_set = set_A & set_B
difference_set = set_A - set_B

print(union_set, intersection_set, difference_set)
