numbers = [3, 5, 7, 9, 11, 13, 15]

print("List:", numbers)
target = int(input("Enter any number: "))
print(f"Searching for: {target}")

for num in numbers:
    if num == target:
        print("Number found")
    else:
        while num != target:
            print("Target not found")
            break