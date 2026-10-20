def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "valueError: cannot divid by zero"
    return a / b

running = True
while running:
    try:
        a = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        b = float(input("Enter second number: "))

    except ValueError:
        print("Invalid number")

    else:   
        if operator == "+":
            print(add(a, b))
        elif operator == "-":
            print(subtract(a, b))
        elif operator == "*":
            print(multiply(a, b))
        elif operator == "/":
            print(division(a, b))
        else:
            print("Invalid operator")
    
    answer = input("Continue? (yes/no): ").lower()

    while answer != "yes" and answer != "no":
        print("Invalid answer. Enter yes or no.")
        answer = input("Continue? (yes/no): ").lower()

    if answer == "no":
        running = False