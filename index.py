print("Welcome to the Pattern Generator and Number Analyzer!")

while(True):
    print("\nSelect an option:")

    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")

    choice=int(input("Enter your chice: "))
    match choice:
        case 1:
            i=int(input("Enter the number of rows for the pattern: "))
            print("\npattern:")
            for i in range(1,i+1):
                for j in range(1,i+1):
                    print("*",end=" ")
                print()
        case 2:
            start=int(input("\nEnter the start of the range: "))
            end=int(input("Enter the end of the range: "))
            
            sum=0
            
            for i in range(start,end+1):
                if(i%2 ==0):
                    print("Number ",i," is even" )
                else:
                    print("Number ",i," is odd" )
                sum=sum+i
            print(f"Sum of all numbers from {start} to {end} is :{sum}")
        case 3:
            print("Exitig the program. Goodbye!")
            break
        case _:
            print("Enter welid choice!!")


