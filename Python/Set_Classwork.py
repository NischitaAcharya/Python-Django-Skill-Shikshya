#WAP to remove dublicacy from list [5,6,7,3,5,6,6,7,8,2,9,2,9] using logic of firts question ( with and without type conversion)

#With using Type conversion
my_set = [5,6,7,3,5,6,6,7,8,2,9,2,9]
unique = set(my_set)
print("List after removing duplicates (With Type Conversion):", unique)


#Without using type conversion

Numbers = [5, 6, 7, 3, 5, 6, 6, 7, 8, 2, 9, 2, 9]

unique = []

for item in Numbers:
    if item not in unique:
        unique.append(item)

print("List after removing duplicates (Without Type Conversion):", unique)

# Set predefined function Practice
# a = {2,3,4}
# b = {3,4,5}
# print(a|b)

# print(a & b)


#WAP the given list {4,5,3,5,6,7,8,3,4,6,9,7,4} without using sort predefined function (assin)

numbers = [4, 5, 3, 5, 6, 7, 8, 3, 4, 6, 9, 7, 4]

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]

print("Sorted list:", numbers)





