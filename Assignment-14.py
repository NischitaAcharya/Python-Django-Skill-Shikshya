#WAP to find Minimum number
#While loop
numbers =  [3, 5, 6, 7]
min_num = numbers[0]

for iterate_num in numbers:
    if iterate_num < min_num:
        min_num = iterate_num
        
print("The manimum number is:", min_num)

#For loop
numbers = [3, 5, 6, 7]
min_num = numbers[0]

for iterate_num in numbers:
    if iterate_num < min_num:
        min_num = iterate_num

print("The minimum number is:", min_num)

#WAP to print square of all number of list [21,54,76,2,1,34,56]  ( using while loop as shown in class)
my_list = [21, 54, 76, 2, 1, 34, 56]

squared_list = []
count = 0
while count < len(my_list):
    squared_list.append(my_list[count] ** 2)
    count += 1

print("square list =", squared_list)


# 4212 4556 5456 2189 = **** **** **** 2189
card_number = "4212 4556 5456 2189"

masked_number = "**** **** **** " + card_number.split()[-1]       #assuming (['4212', '4556', '5456', '2189'][-1]) = 2189 =(card_number.split()[-1])
print(masked_number)



#find even number and store in new list using both (without list comprehension and list comprehension) of [2,4,5,7,8,23,24,22,27] 

#Without list comprehension
numbers = [2, 4, 5, 7, 8, 23, 24, 22, 27]
even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print("Without List Comprehension :" ,even_numbers)

#With list comprehension
numbers = [2, 4, 5, 7, 8, 23, 24, 22, 27]
even_numbers = [num for num in numbers if num % 2 == 0]

print("With List Comprehension :" ,even_numbers)


#WAP to print square number using List comprehension
my_lists = [ 22,34,45,43,23,56]

print("****Using List Comprehension finding Square Number")
square_list = [item*item for item in my_lists]
print(square_list)



