from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_machine = CoffeeMaker()
m_machine = MoneyMachine()

while True:
    inpt = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if inpt == 'off':
        break
    elif inpt == 'report':
        coffee_machine.report()
        m_machine.report()
        continue
    if menu.find_drink(inpt) is None:
        continue
    if not coffee_machine.is_resource_sufficient(menu.find_drink(inpt)):
        continue
    if not m_machine.make_payment(menu.find_drink(inpt).cost):
        continue
    coffee_machine.make_coffee(menu.find_drink(inpt))
print("Coffee machine powering down.")