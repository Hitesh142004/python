num1 = int(input("Enter the Value of N1 :"))
num2 = int(input("Enter the Value of N2 :"))
num3 = int(input("Enter the Value of N3 :"))
num4 = int(input("Enter the Value of N4 :"))

if num1 > num2:
    if num1 > num3:
        if num1 > num4:
            print("Number 1 is Greater")
        elif num4 > num1:
            print("Number 4 is Greater")
        else:
            print("Number 1 and Number 4 are same and Greater.")
    elif num3 > num1:
        if num3 > num4:
            print("Number 3 is Greater")
        elif num4 > num3:
            print("Number 4 is Greater")
        else:
            print("Number 3 and Number 4 are same and Greater.")
    else:
        if num1 > num4:
            print("Number 1 and Number 3 are same and Greater.")
        elif num4 > num1:
            print("Number 4 is Greater")
        else:
            print("Number 1, Number 3 and Number 4 are same and Greater.")

elif num2 > num1:
    if num2 > num3:
        if num2 > num4:
            print("Number 2 is Greater")
        elif num4 > num2:
            print("Number 4 is Greater")
        else:
            print("Number 2 and Number 4 are same and Greater.")
    elif num3 > num2:
        if num3 > num4:
            print("Number 3 is Greater")
        elif num4 > num3:
            print("Number 4 is Greater")
        else:
            print("Number 3 and Number 4 are same and Greater.")

else:
    if num1 > num3:
        if num1 > num4:
            print("Number 1 and Number 2 are same and Greater.")
        elif num4 > num1:
            print("Number 4 is Greater")
        else:
            print("Number 1, Number 2 and Number 4 are same and Greater.")
    elif num3 > num1:
        if num3 > num4:
            print("Number 3 is Greater")
        elif num4 > num3:
            print("Number 4 is Greater")
        else:
            print("Number 3 and Number 4 are same and Greater.")
    else:
        if num1 > num4:
            print("Number 1, Number 2 and Number 3 are same and Greater.")
        elif num4 > num1:
            print("Number 4 is Greater")
        else:
            print("All are Equal")