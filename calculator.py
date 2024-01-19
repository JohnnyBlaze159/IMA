def add(num1: int,num2: int):
    return num1 + num2

def subtract(num1: int,num2: int):
    return num1 - num2

def multiply(num1: int,num2: int):
    return num1 * num2

def divide(num1: int,num2: int):
    return num1 / num2

def caculator():
    print ("Selet operation:")
    print ("1. Add")
    print ("2. Subtract")
    print ("3. Multiply")
    print ("4. Divide")

    choice = input ("Enter Choice (1/2/3/4):")

    num1 = float (input("Enter first number"))
    num2 = float (input("Enter second number"))

    if choice == "1":
        print ("Results", add(num1, num2)) 

    elif choice == "2":
        print ("Results", subtract(num1, num2)) 

    elif choice == "3":
        print ("Results", multiply(num1, num2))

    elif choice == "4":
        print ("Results", divide(num1, num2))

    else
        print ("Invalid input, try again.")


        calculator()