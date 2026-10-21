# 4. Write a program to ,
#     read the value of an integer m    (user input)
#         and display the value of n.

#         n is 1 when m is larger than 0 and -1 when m is less than 0.
# Test Data : -5
# Expected Output :
# The value of n = -1
n=None
m=int(input("Enter the value of an integer m "))

if m < 0:
    n=1
else :
    n=-1
    
print(f"The value of n = {n}")