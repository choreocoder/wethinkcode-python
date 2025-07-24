def main():
    while True:
        try:
            fraction = input("Enter Fraction: ")
            x, y = fraction.split("/")
            x = int(x)
            y = int(y)
            if x <= 0 or y <= 0 or x > y:
                raise ValueError
            percent = convert_to_percentage(x, y)
        except ValueError:
            print("Invalid Value Input!")
            continue
        except ZeroDivisionError:
            print("You can't divide a number by zero!")
            continue

        if percent <= 1:
            print("E")
        elif percent >= 99:
            print("F")
        else:
            print(f"{percent}%")
        break  # Exit loop once valid input processed

def convert_to_percentage(x, y):
    return round((x / y) * 100)

main()
