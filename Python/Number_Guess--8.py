# step 1 : Start
# step 2 : Assign any random number to variable random_number
# step 3 : Guess_count = 0
# step 4 : Take guess input number from User ( User_Guess = 35)
# step 5 : Compare user guess number with random_number
# if User_Guess == random_number then print ("congrats, in {some attempt} you guess")
#break
# Generate random number between 1 and 100 (import random)


# 1st Way

import random

Random_number = random.randint(1, 100)
User_Guess = None
Guess = 0

while (User_Guess != Random_number):
  User_Guess = int(input("Enter your guess (1 to 100): "))
  Guess += 1
  
  if (User_Guess == Random_number):
          print("You guess is correct.")
          
  else:
        if (User_Guess > Random_number):
                  print("Incorrect guess number! Choose a smaller number.")
                  
        else :
                print("Incorrect guess number! Choose a larger number.")
                
print(f"Your guess {Random_number} is Correct! Well Done!")


#2nd Way
# user_guess = int(input("Enter your guess (0 to 100): "))
# if not 0 <= user_guess <= 100:
#     print("Please enter a number between 0 and 100.")
#     continue    ( this can be added to restrict the input between 0 and 100, in case someone types a number out of bounds:)

import random

random_number = random.randint(0, 100)
guess_count = 0

while True:
    try:
        user_guess = int(input("Enter your guess (1 to 100): "))
        guess_count += 1

        if user_guess == random_number:
            print(f"Correct! The number was {random_number}.")
            break
        elif user_guess > random_number:
            print("Too high! Try a smaller number.")
        else:
            print("Too low! Try a larger number.")
    except ValueError:
        print("Please enter a valid integer.")

print(f"You guessed the number in {guess_count} attempts.")

