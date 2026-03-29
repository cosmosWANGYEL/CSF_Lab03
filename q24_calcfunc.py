def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b

while True:
    num1 = float(input("Enter first number: "))
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = int(input("Enter your operator: "))
    num2 = float(input("Enter second number: "))

    if choice == 5:
        print("Exiting.....")
        break

    if choice == 1:
        result = num1 + num2
        print(num1,"+",num2,"=",result)
    elif choice == 2:
        result = num1 - num2
        print(num1,"-",num2,"=",result)
    elif choice == 3:
        result = num1 * num2
        print(num1,"*",num2,"=",result)
    elif choice == 4:
        result = num1 / num2
        print(num1,"/",num2,"=",result)
    else:
        print("Invalid operator!")