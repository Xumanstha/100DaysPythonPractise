MENU={
    "espresso":{
        "ingredients":{
            "water":50,
            "coffee":18,
        },
        "cost":1.5,
    },
    "latte":{
        "ingredients":{
            "water":200,
            "milk":150,
            "coffee":24,
        },
        "cost":2.5,
    },
    "cappuccino":{
        "ingredients":{
            "water":250,
            "milk":100,
            "coffee":24,
        },
        "cost":3.0
    }
}

resources={
    "water":300,
    "milk":200,
    "coffee":100,
    "Money":0,
}

def Report():
    for resource in resources:
        if resource=="water" or resource=="milk":
            unit="ml"
        elif resource=="coffee":
            unit="g"
        else:
            unit="$"
        print(f"{resource}: {resources[resource]}{unit}")

def Check_Resource(coffee):
    resource_fulfilled=True
    for ingredient in coffee["ingredients"]:
        if coffee["ingredients"][ingredient]>resources[ingredient]:
            print(f"Sorry! There is not enough {ingredient} in machine!")
            resource_fulfilled=False
            break
    return resource_fulfilled

def Process_Coins():
    print("Please Insert Coins.")
    quarters=int(input("How many quarters?: "))
    dimes=int(input("How many dimes?: "))
    nickles=int(input("How many nickles?: "))
    pennies=int(input("How many pennies?: "))

    total_value=0.25*quarters+0.10*dimes+0.05*nickles+pennies*0.01
    return total_value

def Check_Transaction(user_money,Coffee):
    cash_fulfilled=True
    if user_money==Coffee["cost"]:
        resources["Money"]+=user_money
    elif user_money>Coffee["cost"]:
        return_money=user_money-Coffee["cost"]
        resources["Money"]+=Coffee["cost"]
        print(f"Here is ${return_money:.2f} dollars in change")
    else:
        print(f"Sorry that's not the enough money. Money is refunded {user_money}")
        cash_fulfilled=False
    return cash_fulfilled

def Make_Coffee(coffee):
    for ingredient in coffee["ingredients"]:
        resources[ingredient]-=coffee["ingredients"][ingredient]
    

def Coffee_Machine():
    on_the_coffee_machine=True
    while on_the_coffee_machine:
        prompt=input("What would you like (espresso/latte/cappuccino): ")

        if prompt=="off":
            on_the_coffee_machine=False
            print("Turning off... Goodbye!")
        
        elif prompt=="report":
            Report()
            print("\n"*5)

        elif prompt in MENU:
            if Check_Resource(MENU[prompt]):
                if Check_Transaction(Process_Coins(),MENU[prompt]):
                    Make_Coffee(MENU[prompt])
                    print(f"Here is your {prompt}. Enjoy!")
                    print("\n"*5)
                else:
                    print("\n"*5)
                    continue
            else:
                continue
        else:
            print("Try again! Invalid prompt")
            print("\n"*5)
            continue

Coffee_Machine()
       


