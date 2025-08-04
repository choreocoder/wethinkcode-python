import inflect

p = inflect.engine() #calling function within inflect library

names = [] #storing input

while True: #keeps asking asking the user until ctrl + d is clicked
    try:
        user_name = input("Enter Name: ").title()
        if user_name not in names:
            names.append(user_name) #adds input to the list
    except EOFError:
        break #breaks out of loop

joined_names = p.join(names) #converts the string and joins words
print("Adieu, adieu, to", joined_names)
