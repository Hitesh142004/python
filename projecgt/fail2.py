# 2. Write a program to check whether a given number is even or odd.
# Test Data : 15
# Expected Output :
# 15 is an odd integer

Number=int(input("Enter the number : "))

if Number % 2==0:
    print(f"{Number}is an even integer.")
else :
    print(f"{Number}is an even odd.")
    