def main():
    text = input("Name: ")
    print(snake_case(text))

def snake_case(text):
    result = ""

    for char in text:
        if char.isupper():
            result += "_" + char.lower()

        else:
            result += char
    return result

main()
