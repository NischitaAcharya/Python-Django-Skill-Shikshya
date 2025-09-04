#WAP to swap variable where a=5,b=8
a = 5
b = 8

a,b = b,a 
print("After swapping:")
print("a =", a)
print("b =", b)

#Another Way ( using temporary value=t)

t = a
a = b
b = t
print("After swapping:")
print("a =", a)
print("b =", b)


#WAP to find maximum number of given positive string number "3746297348937368"or [3,5,6,7,2,8,4,5,6,7,8,2,1]
#step 1 : first take a max_num variable and assign it into minimum number max_num =0
#step 2 : iterate each item and compare each item to max_num, if iterate_num > max_num: max_num = iterate_num
#step 3 : stop
#iterate number means the number like 3, 5,6,7


max_num = 0

numbers = [3, 5, 6, 7]

for iterate_num in numbers:
    if iterate_num > max_num:
        max_num = iterate_num


print("The maximum number is:", max_num)


my_list = [23, 45, 7, 86]

count = 0
while count < len(my_list):
    print(my_list[count])
    count = count + 1



# 4212 4556 5456 2189 = **** **** **** 2189
card_number = "4212 4556 5456 2189"

parts = card_number.split()                 # Split the card number into parts
for i in range(len(parts) - 1):             # Replace all parts except the last one with '****'
    parts[i] = "****"
    
masked_number = " ".join(parts)             # Join the parts back into a string
print(masked_number)



#find even number and store in new list using both (without list comprehension and list comprehension) of [2,4,5,7,8,23,24,22,27] 

#learn and study about dictonary

