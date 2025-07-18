def main():
    text = input("Enter text: ")
    text = text.strip()
    text = convert(text)
    print(text)


def convert(text):
    result = ""
    vowels = "aeiouAEIOU"
    for char in text:
        if char not in vowels:
            result += char


    return result

main()

