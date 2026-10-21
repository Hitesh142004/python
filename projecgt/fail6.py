# 2. Write a  program to check whether a triangle is Equilateral, Isosceles or Scalene.
# Test Data :
# 50 50 60
# Expected Output :
# This is an isosceles triangle.

corner1=int(input("Enter the rediyas of Fast corner : "))
corner2=int(input("Enter the rediyas of Fast corner : "))
corner3=int(input("Enter the rediyas of Fast corner : "))

if corner1==corner2 and corner2==corner3:
    print("This is an Equilateral triangle.")
elif corner1==corner2 or corner2==corner3 or corner3==corner1:
    print("This is an isosceles triangle.")
else:
    print("This is an Scalene triangle.")