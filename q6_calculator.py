num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Enter your operator: "))

if choice == 1:
    result = num1 + num2
    print(num1, "+", num2, "=", result)
elif choice == 2:
    result = num1 - num2
    print(num1, "-", num2, "=", result)
elif choice == 3:
    result = num1 * num2
    print(num1, "x", num2, "=", result)
else:
    result = num1 / num2
    print(num1, "/", num2, "=", result)