#Wap to check given word is palidrome or not [like(level, noon,madam)]
#1.Take input from the user
#2.Check if the word is the same when reversed
#3.Use if and else condition and print


Word = input("Enter a word: ")

if Word == Word[::-1]:
    print("The given word is a palindrome.")
else:
    print("The given word is not a palindrome.")
    

#Another Way:
# Step 1 : Define any word
# Step 2 :Reverse Word [ reverse()  this function can also be used]
# Step 3 :Compare both word (define and reverse word)
# Step 4 : Use if and print
# Step 5: Use else and print


word = "level"
reversed_word = word[::-1]

if word == reversed_word:
    print("Palindrome Word")
else:
    print("Not a palindrome Word")

print(word)



# Another way
# in 4th and 6th line in {word} the given word comes in that place
# and you need to use f after bracket (f(" "))


word = "level"
reversed_word = word[::-1]

if word == reversed_word:
    print(f"the given word {word} is a Palindrome Word") 
else:
    print(f"the given {word} is not a palindrome Word")

print(word)
