#1. Use 2 separate functions. One for the parse conversion and the other for the main.
#2. Define a parse function that takes in a string and converts it to integers.
#3. Split the string and create a variable called "parts" so I can index the values.


def parse_binary(expression):
    parts = expression.split()
    x = int(parts[0])
    y = parts[1]
    z = int(parts[2])
    return x, y, z


def main():
    expression = input("Enter your expression: ")
    x, y, z = parse_binary(expression)
    if y == "+":
        print(float(x + z))
    elif y == "-":
        print(float(x - z))
    elif y == "*":
        print(float(x * z))
    elif y == "/":
        print(float(x / z))
    else:
        print("INVALID EXPRESSION!")


main()
