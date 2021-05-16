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
coffee_machine_on = True


def sufficient_ingredients(input_choice):
    choice = MENU[input_choice]["ingredients"]
    for coffee in MENU:
        if input_choice == "espresso":
            if resources["water"] < choice["water"] or resources["coffee"] < choice["coffee"]:
                return False
            else:
                return True
        else:
            if input_choice == coffee:
                if resources["water"] < choice["water"] or \
                        resources["coffee"] < choice["coffee"] or \
                        resources["milk"] < choice["milk"]:
                    return False
                else:
                    return True


# user choice (espresso/latte/cappuccino) if ingredients available
bank = 0


def coffee_machine(input_choice):
    global bank
    if input_choice == "espresso" or input_choice == "latte" or input_choice == "cappuccino":
        if sufficient_ingredients(input_choice):
            for coffee in MENU:
                if input_choice == coffee:
                    print(MENU[input_choice]["cost"])
                    print("Please insert coins.")

                    quarters = int(input("How many quarters?: "))
                    dimes = int(input("How many dimes?: "))
                    nickles = int(input("How many nickles?: "))
                    pennies = int(input("How many pennies?: "))

                    total_amount_paid = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
                    update_resources(input_choice)
                    sufficient_ingredients(input_choice)
                    if total_amount_paid >= MENU[input_choice]["cost"]:
                        print(f"""Here is ${round(total_amount_paid - MENU[input_choice]["cost"], 2)} in change.""")
                        bank += MENU[input_choice]["cost"]
                    else:
                        print("Sorry that's not enough money. Money refunded.")
        else:
            print("Sorry insufficient ingredients.")
    elif input_choice == "report":
        print(f"""Water: {resources["water"]}ml""")
        print(f"""Milk: {resources["milk"]}ml""")
        print(f"""Coffee: {resources["coffee"]}mg""")
        print(f"""Money: ${round(bank, 2)}""")
    elif input_choice == "off":
        global coffee_machine_on
        coffee_machine_on = False
    else:
        print("Invalid input.")


def update_resources(input_choice):
    for coffee in MENU:
        if input_choice == coffee:
            choice = MENU[input_choice]["ingredients"]
            resources["water"] -= choice["water"]
            resources["coffee"] -= choice["coffee"]
            if input_choice != "espresso":
                resources["milk"] -= choice["milk"]


while coffee_machine_on:
    user_choice = input("What do you want? (espresso/latte/cappuccino): ")
    coffee_machine(user_choice)


# print amount needed to pay

# insert coins

# input quarters, dimes, nickles, pennies

# calculate change or insufficiency

# make changes to resources and bank