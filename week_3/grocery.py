def main():
    grocery_list = {}

    while True:
        try:
            grocery_items = input()
        except EOFError:
            break

        item = grocery_items.lower()

        if item in grocery_list:
            grocery_list[item] += 1
        else:
            grocery_list[item] = 1

    items = list(grocery_list.keys())
    items.sort()

    for item in items:
        count = grocery_list[item]
        print(f"{count} {item.upper()}")

if __name__ == "__main__":
    main()
