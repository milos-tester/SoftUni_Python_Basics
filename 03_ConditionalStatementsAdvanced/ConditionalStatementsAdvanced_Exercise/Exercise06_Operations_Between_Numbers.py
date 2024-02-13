number1 = int(input())
number2 = int(input())
operation = input()

result = 0
operator = ""
even_or_odd = ""
if operation == "+":
    result = number1 + number2
    operator = "+"
    if result % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"
    print(f"{number1} + {number2} = {result} - {even_or_odd}")
elif operation == "-":
    result = number1 - number2
    operator = "-"
    if result % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"
    print(f"{number1} - {number2} = {result} - {even_or_odd}")
elif operation == "*":
    result = number1 * number2
    operator = "*"
    if result % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"
    print(f"{number1} * {number2} = {result} - {even_or_odd}")
elif operation == "/":
    if number2 == 0:
        print(f"Cannot divide {number1} by zero")
    else:
        result = number1 / number2
        print(f"{number1} / {number2} = {result:.2f}")
elif operation == "%":
    if number2 == 0:
        print(f"Cannot divide {number1} by zero")
    else:
        result = number1 % number2
        print(f"{number1} % {number2} = {result}")