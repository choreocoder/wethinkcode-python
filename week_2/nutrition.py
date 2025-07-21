def main():
    fruit_name = input("Enter Fruit: ").title()  
    print(is_fruit(fruit_name))

def is_fruit(fruit_name):
    fruits = {
        "Apple": 130,
        "Avocado": 50,
        "Banana": 110,
        "Cantaloupe": 50,
        "Grapefruit": 60,
        "Grapes": 90,
        "Honeydew Melon": 50,
        "Kiwifruit": 90,
        "Lemon": 15,
        "Lime": 20,
        "Nectarine": 60,
        "Orange": 80,
        "Peach": 60,
        "Pear": 100,
        "Pineapple": 50,
        "Plums": 70,
        "Strawberries": 70,
        "Sweet Cherries": 100,
        "Tangerine": 50,
        "Watermelon": 80
    }
    if fruit_name in fruits:
        return fruits[fruit_name]
    else:
        return ""

main()
