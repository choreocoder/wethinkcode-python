import emoji


def main():
    try:
        user_emoji = input("Enter emoji: ")

        # Check if input is an integer string
        try:
            int(user_emoji)
        except ValueError:
            # Not a number, so continue normally
            pass
        else:
            # Input *is* a number — raise an error to handle
            raise ValueError("Input cannot be a number")

    except (UnicodeEncodeError, UnicodeDecodeError):
        print("Oops..Something went wrong!")
    except ValueError as e:
        print("Oops... You entered a number. Please enter text or emoji codes instead.")
    else:
        print(emoji.emojize(user_emoji, language="alias"))


if __name__ == "__main__":
    main()
