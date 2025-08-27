#Nested condition

#print(age,type(age)) [gives data type]
#int(age)   [converts to integers]

#Wap to take input from user and find age group (child, teen, adult, middle aged, old )



age = int(input("Enter your age: "))

if age <= 12:
    print("You are a child.")
elif age >12 and age <= 19 :
    print("You are a teen.")
elif age > 19 and age <= 35:
    print("You are an adult.")
elif age > 35 and age <= 59:
    print("You are middle-aged.")
elif age > 59 and age <=150:
    print("You are a senior Citizen.")
else:
    print("Invalid")
   