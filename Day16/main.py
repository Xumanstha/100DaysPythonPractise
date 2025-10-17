from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker=CoffeeMaker()
menu=Menu()
money_machine=MoneyMachine()

on_the_coffee_machine=True
while on_the_coffee_machine:
    prompt=input(f"What would you like? {menu.get_items()}  ")
    if prompt=="off":
        print("Bye! Bye!")
        on_the_coffee_machine=False
    elif prompt=="report":
        coffee_maker.report()
        money_machine.report()

    elif menu.find_drink(prompt) is not None:
        coffee=menu.find_drink(prompt)
        print(coffee_maker.is_resource_sufficient(coffee))
        if coffee_maker.is_resource_sufficient(coffee):
            if money_machine.make_payment(coffee.cost):
                coffee_maker.make_coffee(coffee)






