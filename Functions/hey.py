def toppings(*topping):
    print("Making pizza with following toppings.")
    for items in topping:
        print(f"-{items.title()}")