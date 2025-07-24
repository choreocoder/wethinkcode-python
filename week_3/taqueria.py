def main():
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    total = 0 #Variable that stores the total.

    while True: #While Loop will keep prompting user input
        try:
            item = input("Item: ").title() #Title method deals with input later
            if item in menu: #checks if item is in menu (dict)
                total += menu[item] #Adds value to the total
                print(f"${total:.2f}") #.2 handles two decimal places
        except EOFError: 
            break

main()

