#In python, nested loop is a loop that is contained within another loop

# for country in ["Nepal","India","USA"]:
#   print(country)

# Country_Data = [{"Country":"Nepal","States":["Bagmati","Gandaki","Koshi","Madhesh"]},{"Country":"India","States":["Bihar","Mumbhai"]},{}]
# for Country in Country_Data:
#     print(Country)


# infinite loop, with infinite person  
# request hit (google.com)



#WAP 23445 5675 876436 948 this in vertical form as ***** **** ****** 948
# Convert number to string

print("1st One")

number = [23445, 5675, 876436, 948]

for numb in number:       
    digits = str(numb)       
    
    for _ in digits:            # (nested loop)
        print('*', end='')   # Print * for each digit
            
    print() 
    
    
print("2nd One")
                    

numbers = [23445, 5675, 876436, 948]

for i in range(len(numbers)):
    num = numbers[i]
    digits = str(num)  

    if i == len(numbers) - 1:
        print(num)  
    else:
        # Inner loop (nested) to print stars for each digit
        for _ in digits:
            print('*', end='')
        print() 
