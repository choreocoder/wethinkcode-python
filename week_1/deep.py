def main():
    question = input("What is the answer to the question of Life, The universe, and Everything? ")
    question = question.strip().lower()

    if question == "42" or question == "forty two" or question == "forty-two":
        print("Yes")
    else:
        print("No")

main()
