def convert():
    amount_inserted = 0
    coke_price = 50

    while amount_inserted < 50:
        coin = int(input("Enter Coin: "))

        if coin == 25 or coin == 10 or coin == 5:
            amount_inserted += coin
        else:
            print("Invalid Coin!")

        if amount_inserted < 50:
            print("Amount Due:", 50 - amount_inserted)

    print("Change Owed:", amount_inserted - 50)


convert()
