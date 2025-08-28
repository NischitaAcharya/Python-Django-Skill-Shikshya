#WAP to find prime number of user input number

#Practice ( classwork)

# number = int(input("Enter any number: "))
# count = 1    
# while count <= number:
#     print(count)
#     count += 1
    

number = int(input("Enter any number: "))
count = 1   
divisible_count = 0 
while count <= number:
    
    if number%count == 0:
        divisible_count += 1
    
    count += 1 
    
print("divisible_count",divisible_count )   

if divisible_count <=2:
    print(number,f"is prime number with divisible count {divisible_count}")
else:
    print(number,f"is not prime number because its divisible count {divisible_count}")

        
        
#Another Way


# num = int(input("Enter a number: "))

# if num <= 1:
#     print(num, "is not a prime number.")
# else:
#     is_prime = True
#     for i in range(2, num):
#         if num % i == 0:
#             is_prime = False
#             break

#     if is_prime:
#         print(num, "is a prime number.")
#     else:
#         print(num, "is not a prime number.")




# Prime number check using square root method
# Take input from user
# 0 and 1 are not prime numbers

import math

num = int(input("Enter a number: "))

if num <= 1:
    print(num, "is not a prime number.")
else:
    is_prime = True
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, "is a prime number.")
    else:
        print(num, "is not a prime number.")
        
        
        
        

#WAP to find prime number from 5 to 20

for num in range(5, 21):
    is_prime = True  # Assume the number is prime
    
    if num < 2:
        is_prime = False
    else:
        for i in range(2, int(num ** 0.5) + 1):  #[(17 ** 0.5) acn also ne written as square root of 17(squt.17)
            if num % i == 0:            #( here i is number between 2-5=3,4 and check if 17 is divied by that if no the prime and if yes the not prime)
                is_prime = False
                break
    
    if is_prime:
        print(num)

        

