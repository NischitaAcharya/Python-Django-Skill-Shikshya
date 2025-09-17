#WAP to make a calculator
#step : Take input first number from user
#step : Take input operator (+,_,*,/)
#step : Take input second number from user
#(try:
# 5/0
# except
# print("cannot divide by Zero"))


Number_1 = float(input("Enter the first number: "))

operator = input("Enter operator (+, -, *, /): ")

Number_2 = float(input("Enter the second number: "))

if operator == '+':
    result = Number_1 + Number_2
elif operator == '-':
    result = Number_1 - Number_2
elif operator == '*':
    result = Number_1 * Number_2
elif operator == '/':
    if Number_2 != 0:
        result = Number_1 / Number_2
    else:
        result = "Error! Cannot divide by zero."
else:
    result = "Invalid operator!"

print("Result:", result)



