#WAP to print square of prime number upto 200, if prime number is 13 then skip, if prime number 59 then exit the program
# Check if num is prime using square root method
# Stop the loop at 59
# Print square of the prime number

for num in range(201):
    
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        if num == 13:
            continue  
        if num == 59:
            break     
        print(num )  



  

