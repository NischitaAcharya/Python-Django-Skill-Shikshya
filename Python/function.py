# def design():
#     lines = """
#      ******
#      1. sum
#      2. Subtract
#      3. Multiply
#      ******
# """
#     # print(lines)
#     return lines

#     # while True:   ( this runs infinite program)
#     # design()
    
# values = design()
# print(values)


#How to add argument
def sum(first_num,second_num):
    # print(first_num,second_num)
    sum = first_num+second_num
    # print(sum)
    return sum      #(return type with argument)
    
result = sum(4,6)
print(result)

#Temperature detect

import random

def temperature_detect():
    # return 20
    temperature = random.randint(1,100)
    # print(temperature,"Inside Function")
    return temperature
    

def moisture():
    # return 60
    return random.randint(1,100)

def probability_for_rain(temperature,moisture):
    #predict
    # return 70
    return (temperature+moisture)*(100/200)

temperature = temperature_detect()
# print(temperature,"After Called function value")  [ to print temperature only]
moisture_value = moisture()

probability = probability_for_rain(temperature, moisture_value)
print("Today Probability for rain is:",probability,"%")



#WAP to make a calculator using function(return type with argument)

def add(a, b):         # <-- 'a' and 'b' are arguments
    return a + b       # <-- 'return' sends back the result 

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero."
    
print("Simple Calculator")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == '1':
    result = add(num1, num2)
    print("Result:", result)
elif choice == '2':
    result = subtract(num1, num2)
    print("Result:", result)
elif choice == '3':
    result = multiply(num1, num2)
    print("Result:", result)
elif choice == '4':
    result = divide(num1, num2)
    print("Result:", result)
else:
    print("Invalid input")
