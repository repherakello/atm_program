import random


target = random.randint(0,9)
while True:
    guessed_number = eval(input("Guess a number"))
    if guessed_number == target:
        print("Bravo! youve guessed it correctly,the number was: ",target)
        break
    elif guessed_number > target:
        print("Too high try again!")
    elif guessed_number < target:
        print("Too low try again!")
    else:
        print("Invaled input")
print("Thank you for trying your luck!")