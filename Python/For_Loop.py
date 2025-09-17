# for letter in "Python":
#     print(letter)
    

#WAP to check each item of numbers is odd or even
numbers = "123456789"

for num in numbers:
    digit = int(num)
    if digit % 2 == 0:
        print(f"{digit} is even")
    else:
        print(f"{digit} is odd")
        

number = "123456789"
if number % 2 == 0:
    print(f"{number} number is even.")
else:
    print(f"{number} number is odd.")


#WAP to give feed to a person
#if he eats 1 plate then print "all good"
#if he eats 5 plate then "Fat"
#if he eats greater more that 10 plate the print "Tata Bye Bye, BOOM!!"

for plate_count in range (1,40):
    if plate_count == 1:
      print("all good")
    elif plate_count ==5:
        print("Fat")
    elif plate_count >= 10:
        print("Tata Bye Bye, BOOM!!")
        break


#WAP to print all even number from 0 to 100 using range step
#range (start, stop, step)

for num in range(0, 101, 2):
    print(num)
    
