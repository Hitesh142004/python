# Write a Program in Python to create a menu-driven fast-food order system using the 'match case' feature.

# - For example:
# - Press 1 to order a Sandwich
# - Press 2 to order a Pizza
# - Press 3 to order a Burger
# - Extend this program by adding a nested match case for each menu item’s subtype selection by the user.

# - For example:
# - Press 1 for Thin Crust Pizza
# - Press 2 for Cheese Burst Pizza
# - Press 3 for Fresh Dough Pizza

print(" "*12,"welcome to BURGER WALA")
print(" "*20,"MENU"," "*20)
while(True):
    
    print("- Press 1 to order a Sandwich")
    print("- Press 2 to order a Pizza")
    print("- Press 3 to order a Burger")
    print("- press 4 to camlit your oder\n")

    choise=int(input("Enterd your choise : "))

    match choise:
        case 1:
            print("peles select your sandwich .")
            print("- press 1 to masala sandwich ")
            print("- press 2 to cheese chili sandwich")
            print("- press 3 to veg cheese sandwich\n")
            sandwich=int(input("Enterd your choise : "))
        case 2:
            print("peles select your pizza.")
            print("- Press 1 to Thin Crust Pizza")
            print("- Press 2 to Cheese Burst Pizza")
            print("- Press 3 to Fresh Dough Pizza\n")
            pizza=int(input("enterd your choise: "))
        case 3:
            print("peles select your burger.")
            print("- press 1 to veg burger")
            print("- press 2 to mayonis burger")
            print("- press 3 to tanduri burger")
            burger= int(input("enterd your choise: "))
        case 4:
            break
        case _:
            print("peles enterd welid choise!")

print("your oder was acseptes !!")




    