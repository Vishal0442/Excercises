#User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct,
#on successful guess, user will get a "Well guessed!" message, and the program will exit

import random

while True:
    a = random.randint(1,9)
    b = int(input("Guess a number : "))

    if a == b:
        print ("Congrats!! Well Guessed...\n")
        break
    else:
        print ("Oops...Wrong Guess!! Try again...\n")










