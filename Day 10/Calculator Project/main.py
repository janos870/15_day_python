from art import logo

print(logo)

def add(n1, n2):
    return n1 + n2

def subtraction(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operator = {
    "+": add,
    "-": subtraction,
    "*": multiply,
    "/": divide
}

def calculator():
    continue_calculate = True
    n1 = float(input("Enter the first number: "))

    while continue_calculate:
        op = input("Enter an operator (+, -, *, /): ")
        n2 = float(input("Enter the second number: "))

        if op in operator:
            result = operator[op](n1, n2)
            print(f"{n1} {op} {n2} = {result}")
        else:
            print("Invalid operator")

        choice = input(f"Do you want to continue calculate with {result}? (y/n): ").lower()

        if choice == "y":
            n1 = result
        else:
            continue_calculate = False
            print("\n" * 20)
            calculator()

calculator()

