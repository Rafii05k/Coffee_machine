MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0


def process_coins():
    total = int(input("how many quarters?")) * 0.25
    total += int(input("how many dimes?")) * 0.1
    total += int(input("how many pennies?")) * 0.05
    total += int(input("how many Nickles?")) * 0.01
    return total


def is_resource_sufficient(ingredient_of_drink):
    """ checks if there is sufficient ingredient to make the drink"""
    for item in ingredient_of_drink:
        if ingredient_of_drink[item] > resources[item]:
            print(f"sorry, not enough {item}")
            return False

    return True


def is_transaction_successful(money_received, cost):
    """ checks if the money received is enough to buy a drink """
    if money_received < cost:
        print("Sorry, the money is not enough. money refunded!")
        return False
    else:
        change = round(money_received - cost, 2)
        print(f"Here is ur ${change} change")
        global profit
        profit += cost
        return True


def make_coffe(drink_name,drink_ingredient):
    """ updates the resource status plus it serves the coffe"""
    for item in drink_ingredient:
        resources[item]-=drink_ingredient[item]
    print(f"Here is your {drink_name}☕. Enjoy it!")


is_on = True
while is_on:
    order = input("what would u like to order?(latte/cappuccino/espresso)")
    drink = MENU.get(order)
    # the "off" keyword turns of the machine
    if order == "off":
        is_on = False
    elif order == "report":
        print(f"Milk: {resources["milk"]}ml ")
        print(f"Water: {resources["water"]}ml")
        print(f"coffee: {resources["coffee"]}mg")
        print(f"Money: {profit}")
    else:
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment,drink["cost"]):
                make_coffe(order, drink["ingredients"])


