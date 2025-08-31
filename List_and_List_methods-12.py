#Data Structure - List
my_list = [1, 2, 3, 4]

#1. append() - Adds an item to the end of the list.

fruits = ['apple', 'banana']
fruits.append('orange')
print(fruits) 


#2. insert(index, item) - Inserts an item at a specific index.

fruits = ['apple', 'banana']
fruits.insert(1, 'grape')
print(fruits) 

#3. remove (items) - Removes the first matching item.

fruits = ['apple', 'banana', 'banana']
fruits.remove('banana')
print(fruits) 

#4. pop([index]) - Removes and returns item at given index. Default is last.

fruits = ['apple', 'banana', 'cherry']
fruit = fruits.pop()
print(fruit)   # 'cherry'
print(fruits)  # ['apple', 'banana']

#5. index(item) - Returns the index of the first occurrence of the item.[according to position(0,1,2)]

numbers = [10, 20, 30]
print(numbers.index(20))

#6. count(item) - Counts how many times the item appears.

numbers = [1, 2, 2, 3, 2]
print(numbers.count(2))

#7. sort() - Sorts the list in ascending order

numbers = [3, 1, 2]
numbers.sort()
print(numbers)

#8. reverse() - Reverses the list order

numbers = [1, 2, 3]
numbers.reverse()
print(numbers)

#9. copy() - Returns a copy of the list

a = [1, 2, 3]
b = a.copy()
print(b)

#10. clear() - Removes all items from the list

fruits = ['apple', 'banana']
fruits.clear()
print(fruits) 
