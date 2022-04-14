first = input("Enter the first number: ")
second = input("second number: ")
operator = input("Enter a operator(+,-,*,/,%) : ")


first = int(first)
second = int(second)

if operator == "+":
    print(first + second)
elif operator == "-":
    print(first - second)
elif operator == "*":
    print(first * second)
elif operator == "/":
    print(first / second)
elif operator == "%":
    print(first % second)
    print("invalid operation")

