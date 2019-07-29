item = ""
while item != "quit":
    print("Enter an item to check the price: ")
    item = input()

    if item == "pizza":
        print("$3 per slice")
    elif item == "alchohol":
        print("You don't look 21 or over, so no need to give you that information.")
    elif item == "chicken":
        print("We have many chicken options! Chicken nuggets is $5, chciken strips is $8, and chicken fingers are $8.75!")
    else:
        print("We don't have that.")