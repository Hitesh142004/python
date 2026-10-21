# 1. Write a  program to read temperature in centigrade and display a suitable message according to the temperature state below:
# Temp < 0 then Freezing weather
# Temp 0-10 then Very Cold weather
# Temp 10-20 then Cold weather
# Temp 20-30 then Normal in Temp
# Temp 30-40 then Its Hot
# Temp >=40 then Its Very Hot
# Test Data :
# 42
# Expected Output :
# Its very hot.

Temp= int(input("Enter the temperature: "))

if Temp < 0:
    print("Then Freezing weather")
elif Temp >= 0 and Temp <= 10 :
    print("Then Very Cold weather")
elif Temp >= 10 and Temp <= 20 :
    print("Then Cold weather")
elif Temp >= 20 and Temp <= 30 :
    print("Then Normal in Temp")
elif Temp >= 30 and Temp <= 40 :
    print("Then Its Hot")
else:
    print("then Its Very Hot")

