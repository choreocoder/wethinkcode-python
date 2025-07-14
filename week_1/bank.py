def main():
    greeting = input("Hello there! ")
    greeting = greeting.strip().casefold().lower()
    if greeting == "hello":
        print("$0")
    elif greeting.startswith("h"):
        print("$20")
    else:
        print("$100")

main()

