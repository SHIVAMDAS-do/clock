first = input("enter the fast number: ")
second = input("Enter the second number: ")
operator = input("Enter a operator(+,-,*,/,%)")
first = int(first)
second = int(second)

if operator == "+":
    print(first+second)
elif operator == "-":
    print(first-second)
elif operator == "*":
    print(first*second)
elif operator == "/":
    print(first/second)
elif operator == "%":
    print(first%second)
else:
    print("invalid operation")
