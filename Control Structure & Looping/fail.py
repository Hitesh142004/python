number1=int(input("enter the first number: "))
number2=int(input("enter the second number: "))
number3=int(input("enter the third number: "))
number4=int(input("enter the fourth number: "))

if number1>number2:
    if number1>number3:
        if number1>number4:
            print("Number 1 is gretar ")
        elif number1==number4:
            print("Number 1 and 4 is gretar and equal ")
        else:
            print("Number 4 is gretar")
    elif number3>number4:
            if number3==number1:
                print("Number 1 and 3 is gretar and equal")
            else:
                print("Number 3 is gretest ")
    else:
            print("Number 4 is greteast ") 
elif number2>number3:
    if number2>number4:
        if number2>number1:
            print("Number 2 is gretar ")
        elif number2==number1:
            print("Number 1 and 2 is gretar and equal ")
    elif number3>number4:
            print("Number 4 is gretest ")
    else:
            print("Number 1 is greteast ") 
elif number3>number4:
    if number3>number1:
        if number3>number2:
            print("Number 3 is gretar ")
        elif number3==number2:
            print("Number 3 and 2 is gretar and equal ")
    elif number3>number1:
            print("Number 1 is gretest ")
    else:
            print("Number 2 is greteast ") 
elif number4>number1:
    if number4>number2:
        if number4>number3:
            print("Number 4 is gretar ")
        elif number4==number3:
            print("Number 3 and 4 is gretar and equal ")
    elif number4>number2:
            print("Number 2 is gretest ")
    else:
            print("Number 3 is greteast ") 
