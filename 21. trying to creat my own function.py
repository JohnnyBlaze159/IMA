def add(a,b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a,b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply (a,b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide (a,b):
    print(f"DIVIDING {a} / {b}")
    return a / b

num1 = 24
num2 = 34
num3 = 100
num4 = 1023

# 24 + 34 / 100 - 1023
result = add (num1, subtract (divide (num2, num3), num4))
print (result)
print ("omg, Jordan, finally I did it!")