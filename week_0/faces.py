#Give Python the rule I will use
def convert(text):
    text = text.replace(":)","🙂").replace(":(", "🙁")
    return text

#Start programme by prompting user
def main():
    message = input("Hello, How are you feeling today? ")
    converted_message = convert(message)
    print(converted_message)

main()

#Python will never return something that you did not call.
#Always identify clearly
#Tools and reults must always merge
