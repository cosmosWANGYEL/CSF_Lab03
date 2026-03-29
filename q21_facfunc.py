def fac_func(num):
     if num < 0:
          return True
     else:
        factorial = 1
        for i in range(1, num + 1):
            factorial *= i
        return factorial
num = int(input("Enter a number: "))
result = fac_func(num)
print(f"{num}! = {result}")
