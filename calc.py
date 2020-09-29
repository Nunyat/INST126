print("Choose an operation.")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
# Take input from the user 
choice = input("Enter choice(1/2/3/4): ")
num1 = float(input("Enter first number (Should be in numeric form): "))
num2 = float(input("Enter second number (Should be in numeric form): "))
if choice == '1':
    #This function adds two numbers
    print(num1,"+",num2,"=", num1+num2)
elif choice == '2':
    #This function subtracts two numbers
    print(num1,"-",num2,"=", num1-num2)
elif choice == '3':
    #This function multiplies two numbers
    print(num1,"*",num2,"=", num1*num2)
elif choice == '4':
    #This function divides two numbers
    print(num1,"/",num2,"=", num1/num2)
#This function returns error if input is not in the option
else:
    print("Invalid input")