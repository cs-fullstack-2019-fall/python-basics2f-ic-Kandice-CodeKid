# ### Problem 1:
# Write the code to create a random number from 1 - 100. Print the number generated.
#
# ```
# Hint:
# import random
# randomNumber = random.randint(?, ?)
# ```

# import random
# random_number = random.randint(1, 100)
# print(random_number)



#
# ### Problem 2:
# ##### We will keep having this problem until EVERYONE gets it right without help
# Write some python code that has a loop that prompts the User for string input, and will only stop after the User enters ```q```. If the user doesn't enter ```q```, then prompt them to input another string. Continuing asking for input until they enter ```q```.
#
# *NOTE: Your code should handle both lower and uppercase ```q``` values.
#
# stringInput = input("Enter something, or press q to quit")
# while (stringInput.lower() != 'q'):
#     stringInput = input("Enter something, or press q to quit")  #or .lower at the end of the string
#



# ### Problem 4:
# Write some Python code that creates a random number from 1 - 10 and stores it in a variable. Ask the user to guess the random number. Keep letting the user guess until they get it right, then quit. Print the message ```Sorry, incorrect``` for each wrong guess.
#
import random
random_number = random.randint(1, 10)
guess_random = " "
x = random_number

while random_number != guess_random:
    guess_random = int(input("Guess the random number"))
    if random_number != guess_random:
        print("sorry incorrect")
        if guess_random > random_number:
            print('TOO HIGH')
        else:
            print('TOO Low')
else:
    print('You got it')



# #### Extra:
# But the range for the secret random number to 1 - 100. For each wrong guess, include a clue to the Guesser as to if their missing guess was 'too low' or 'too high'.
