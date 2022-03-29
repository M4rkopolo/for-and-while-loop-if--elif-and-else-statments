MENU = {
    "Espresso": {
        "Ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "Latte": {
        "Ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "Cappuccino": {
        "Ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

RESOURCES = {
    "water": 3000,
    "milk": 2000,
    "coffee": 1000,
}
CASH = {
    "money":0,
}
COFFEE_ON_GOING = True


def raport():
    for item in RESOURCES:
        print(f"{item} : {RESOURCES[item]}")
    print(f"{CASH} : {CASH['money']}")
    print("End of the raport")
    return


def off():
    global COFFEE_ON_GOING
    COFFEE_ON_GOING = False


def toss_the_coin(coffee):
    print(f"Please, insert the coins for {coffee}, it cost {MENU[coffee]['cost']}")
    money_quarter = int(input("how many quarters?:"))
    money_dimes = int(input("how many dimes?:"))
    money_nickles = int(input("how many nickles?:"))
    money_pennies = int(input("how many pennies?:"))
    money = 0.1*money_dimes + 0.25*money_quarter + 0.05 * money_nickles + 0.01 * money_pennies
    if money < MENU[coffee]['cost']:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        if money > MENU[coffee]['cost']:
            money -= MENU[coffee]['cost']
            print(f"Here is ${round(money)} in change.")
            CASH["money"] += MENU[coffee]['cost']
        else:
            CASH["money"] += MENU[coffee]['cost']
        return True


def make_coffee(coffee):
    enough = True
    for item in MENU[coffee]["ingredients"]:
        if MENU[coffee]["ingredients"][item] > RESOURCES[item]:
            print(f"Sorry there is not enough {item}.")
            enough = False
    if enough:
        if toss_the_coin(coffee):
            for item in MENU[coffee]["ingredients"]:
                RESOURCES[item] -= MENU[coffee]["ingredients"][item]
            print("Here is your latte ☕️. Enjoy!")
    return


def coffee_machine(option):
    if option == "raport":
        raport()
    elif option == "off":
        off()
    elif option == "espresso" or option == "latte" or option == "cappuccino":
        make_coffee(option)
    return


while COFFEE_ON_GOING:
    answer = input("What would you like? (espresso/latte/cappuccino): ")
    coffee_machine(answer)




