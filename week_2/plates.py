def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    return (
        has_valid_length(s)
        and starts_with_two_letters(s)
        and has_only_alphanumerics(s)
        and numbers_only_at_end(s)
    )

def has_valid_length(s):
    return 2 <= len(s) <= 6

def starts_with_two_letters(s):
    return len(s) >= 2 and s[0].isalpha() and s[1].isalpha()

def numbers_only_at_end(s):
    for i in range(len(s)):
        if s[i].isdigit():
            letters_part = s[:i]
            numbers_part = s[i:]
            break
    else:
        return True

    if not letters_part.isalpha():
        return False
    if not numbers_part.isdigit():
        return False
    if numbers_part.startswith("0"):
        return False

    return True

def has_only_alphanumerics(s):
    return s.isalnum()

main()


