from random import randint

# Prompt user for a valid level (must be a positive integer)
while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except ValueError:
        pass  # If user enters non-integer, do nothing and loop again

# Generate random number between 1 and level
num = randint(1, level)

# Repeatedly prompt the user to guess
while True:
    try:
        guess = int(input("Guess: "))
        if guess <= 0:
            continue  # Ignore non-positive guesses
        if guess > num:
            print("Too large!")
        elif guess < num:
            print("Too small!")
        else:
            print("Just right!")
            break
    except ValueError:
        continue  # Ignore invalid input (like letters, symbols)
