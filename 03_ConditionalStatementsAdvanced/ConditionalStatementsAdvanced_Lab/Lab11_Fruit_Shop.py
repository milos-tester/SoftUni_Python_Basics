fruit_input = input()
day_input = input()
quantity = float(input())

price = 0

if day_input == "Monday" or day_input == "Tuesday" or day_input == "Wednesday" or day_input == "Thursday" or day_input == "Friday":
    if fruit_input == "banana":
        price = 2.50
        result = quantity * price
        print(f'{result:.2f}')
    elif fruit_input == "apple":
        price = 1.20
        result = quantity * price
        print(f'{result:.2f}')
    elif fruit_input == "orange":
        price = 0.85
        result = quantity * price
        print(f'{result:.2f}')
    elif fruit_input == "grapefruit":
        price = 1.45
        result = quantity * price
        print(f'{result:.2f}')
    elif fruit_input == "kiwi":
        price = 2.70
        result = quantity * price
        print(f'{result:.2f}')
    elif fruit_input == "pineapple":
        price = 5.50
        result = quantity * price
        print(f'{result:.2f}')
    elif fruit_input == "grapes":
        price = 3.85
        result = quantity * price
        print(f'{result:.2f}')
    else:
        print('error')
elif day_input == "Saturday" or day_input == "Sunday":
    if fruit_input == "banana":
        price = 2.70
        result = quantity * price
        print(f'{result:.2f}')
    elif fruit_input == "apple":
        price = 1.25
        result = quantity * price
        print(f'{result:.2f}')
    elif fruit_input == "orange":
        price = 0.90
        result = quantity * price
        print(f'{result:.2f}')
    elif fruit_input == "grapefruit":
        price = 1.60
        result = quantity * price
        print(f'{result:.2f}')
    elif fruit_input == "kiwi":
        price = 3.00
        result = quantity * price
        print(f'{result:.2f}')
    elif fruit_input == "pineapple":
        price = 5.60
        result = quantity * price
        print(f'{result:.2f}')
    elif fruit_input == "grapes":
        price = 4.20
        result = quantity * price
        print(f'{result:.2f}')
    else:
        print('error')
else:
    print('error')