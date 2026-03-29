def check_func(num):
   return num % 2 == 0

num = int(input("Enter a number: "))
if check_func(num):
   print("The number is even")
else:
   print("The number is odd")