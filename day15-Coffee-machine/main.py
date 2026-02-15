

coffee = {
    "espresso": {"water":50, "coffee":18, "price":1.5},
    "latte":{"water":200, "milk":150, "coffee":24, "price":2.5},
    "cappuccino":{"water":250, "milk":100, "coffee":24, "price":3.0}
}

resources = {"water":300, "milk":200, "coffee":100, "money":0}

coins = {"quarters":0.25, "dimes":0.10, "nickels":0.05, "pennies":0.01}

def check_resources(order):
    for item in coffee[order]:
        if item != "price":
            if coffee[order][item] > resources[item]:
                print(f"Sorry there is not enough {item}.")
                return False
    return True


def proccess_coins(order):
    total = 0
    quarters = int(input("How many quarters?: "))
    total += quarters * coins["quarters"]
    dimes = int(input("How many dimes?: "))
    total += dimes * coins["dimes"]
    nickels = int(input("How many nickels?: "))
    total += nickels * coins["nickels"]
    pennies = int(input("How many pennies?: "))
    total += pennies * coins["pennies"]
    if total < coffee[order]["price"]:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        change = round(total - coffee[order]["price"], 2)
        print(f"Here is ${change} in change.")
        resources["money"] += coffee[order]["price"]
        for item in coffee[order]:
            if item != "price":
                resources[item] -= coffee[order][item]
        print(f"Here is your {order}. Enjoy!")
        return True

end=False

while not end:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")
    elif choice == "off":
        end = True
    elif choice in coffee:
        if not check_resources(choice):
            continue

        print("Please insert coins.")
        if not proccess_coins(choice):
            continue
    else:
        print("Invalid choice.")