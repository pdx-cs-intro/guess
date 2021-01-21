# Guess The Number game
# Bart Massey 2021

from random import *

secret_range = 10
secret = randrange(secret_range) + 1

done = False
while not done:
    guess = int(input(
        "Guess my number between 1 and " + str(secret_range) + "? "
    ))
    if guess == secret:
        print("Right. You win!")
        done = True
    elif guess > secret:
        print("Try lower…")
    else:
        print("Try higher…")
