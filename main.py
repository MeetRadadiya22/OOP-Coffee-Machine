from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine = True
objMenu = Menu()
objCoffee_maker = CoffeeMaker()
objMoney = MoneyMachine()

while machine == True:
  # menu object from package menu
  choice = input(f"what would you like to order {objMenu.get_items()}?: ")
  # coffeem obj from class CoffeeMaker and package coffee_maker
  if choice == "report":
    objCoffee_maker.report()
    objMoney.report()
  elif choice == "off":
    machine = False
  else:
    # checks the resources are enough or not
    coffee = objMenu.find_drink(choice)
    resources_enough = objCoffee_maker.is_resource_sufficient(coffee)
    print(resources_enough)
    if resources_enough == False:
      machine = False
    else:
      # checks the payment is enough or not
      payment_enough = objMoney.make_payment(coffee.cost)
      if payment_enough == False:
        machine = False
      else:
        # coffee is prepared.
        objCoffee_maker.make_coffee(coffee)
        












  

