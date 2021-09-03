from random import randint
# Generate one random number between 20 and 30
secret = randint(20, 30)

# unique user input
user_inputs = []
# count the number of guesses
guess_count = 3
# Guess limit
guess_limit = len(user_inputs)
print("I am thinking of a number between 20 and 30")

# Run until the limit is reached
try:
    while guess_limit < guess_count:
        # prompt user to guess
        guess = int(input("Guess the number: "))
        # Check whether user guessed correctly or not
        if guess not in user_inputs and guess != secret:
            # adds user guesses to the user input list
            user_inputs.append(guess)
            guess_count -= 1
            if guess < secret and guess_limit < guess_count:
                print('Too small try again')
            elif guess > secret and guess_limit < guess_count:
                print('Too large try again')

        elif guess in user_inputs:
            print("guess different number")

        else:
            print("You won!")
            break

    else:
        print("sorry you failed")
except(TypeError, ValueError):
    print("Invalid entry, try again")