def check_num(num):
    if num % 2 == 0:
        return "The number is even"
    else:
        return "The number is odd"
x = int(input("Enter a number: "))
for i in range(1, x + 1):
    result = check_num(i)
print(f"{i} = {result}")