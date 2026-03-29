marks = float(input("Enter your marks: "))

if marks >= 80:
    print("Your grade is A")
elif 79 >= marks >= 60:
    print("Your grade is B")
elif 59 >= marks >= 40:
   print("Your grade is C")
else:
    print("FAIL")