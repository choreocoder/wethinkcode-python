import random


def main():
    score = 0 #stores the values that will be added later
    level = get_level()  #Calls the get_level() function

    for _ in range(10): #iterates 10 times
        x = generate_integer(level) #converts strings to integers
        y = generate_integer(level)

        tries = 0
        correct = False

        while tries < 3:  #Handles the maximum tries = 3
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == x + y:
                    score += 1
                    correct = True
                    break
                else:
                    print("EEE")
                    tries += 1
            except ValueError:
                print("EEE")
                tries += 1

        if not correct:
            print(f"{x} + {y} = {x + y}")

    print(f"Score: {score}")


def get_level():
    while True: #Keep iterating until it receives level
        try:
            user_level = int(input("Level: "))
            if user_level in [1, 2, 3]: #A list of desired input > Long conditional
                return user_level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9) #Randint provides integers within given range
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError("Invalid level")


if __name__ == "__main__":
    main()
