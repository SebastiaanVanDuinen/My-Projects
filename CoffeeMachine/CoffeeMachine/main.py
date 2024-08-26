from menu import MENU
from menu import resources


start_of_machine = True
resources['money'] = 0


def resources_check():
    for i in MENU[choice]["ingredients"]:
        while MENU[choice]["ingredients"][i] > resources[i]:
            print(f"There is not enough {i}, please refill at least {MENU[choice]["ingredients"][i] - resources[i]}")
            resources[i] += int(input(f"Refill this amount: "))


def process_coins():
    """Returns the total money paid"""
    total = int(input("quarters: ")) * 0.25
    total += int(input("dimes: ")) * 0.1
    total += int(input("nickles: ")) * 0.05
    total += int(input("pennies: ")) * 0.01
    return total


def insufficient_coins(total_payment):
        print(f"You have given a total of ${total_payment}")
        needed_amount = round(MENU[choice]['cost'] - total_payment, 2)
        print(f"You will still need to add ${needed_amount} in order to buy this coffee")


def refill():
    """Refills the amount of resources to a desired amount"""
    for y in resources:
        resources[y] += int(input(f"Refill {y} with this amount: "))


def report():
    for y in resources:
        print(f"{y}: {resources[y]}")


def refund(total):
    refund_amount = round(total_payment - MENU[choice]['cost'], 2)
    print(f"You have put in a total of ${total}. Here is ${refund_amount} in change.")


def make_coffee():
    for x in MENU[choice]["ingredients"]:
        resources[x] -= MENU[choice]["ingredients"][x]

while start_of_machine:
    total_payment = 0
    choice = input(f"What coffee would you like? '{list(MENU.keys())[0]}', '{list(MENU.keys())[1]}' or '{list(MENU.keys())[2]}': ")
    if choice == "shutdown":
        break
    elif choice == "report":
        report()
    elif choice == "cashout":
        print(f"You've cashed out ${resources['money']}")
        resources['money'] = 0
    elif choice == "refill":
        refill()
    else:
        resources_check()
        print(f"The price for a latte is ${MENU[choice]['cost']}\nPlease pay in quarters, dimes, nickles and pennies:")
        while total_payment < MENU[choice]['cost']:
            # coin input:
            total_payment += round(process_coins(), 2)
            if total_payment < MENU[choice]['cost']:
                insufficient_coins(total_payment)
        if total_payment > MENU[choice]['cost']:
            refund(total_payment)
        make_coffee()
        resources["money"] += MENU[choice]["cost"]
        print(f"Here is your {choice}. Enjoy!")