group_budget = int(input())
season = input()
number_of_fishermen = int(input())

price = 0

if season == "Spring":
    price = 3000
    if number_of_fishermen <= 6:
        price *= 0.90
        if number_of_fishermen % 2 == 0:
            price *= 0.95
    if number_of_fishermen > 6 and number_of_fishermen <= 11:
        price *= 0.85
        if number_of_fishermen % 2 == 0:
            price *= 0.95
    if number_of_fishermen > 12:
        price *= 0.75
        if number_of_fishermen % 2 == 0:
            price *= 0.95
elif season == "Summer":
    price = 4200
    if number_of_fishermen <= 6:
        price *= 0.90
        if number_of_fishermen % 2 == 0:
            price *= 0.95
    if number_of_fishermen > 6 and number_of_fishermen <= 11:
        price *= 0.85
        if number_of_fishermen % 2 == 0:
            price *= 0.95
    if number_of_fishermen > 12:
        price *= 0.75
        if number_of_fishermen % 2 == 0:
            price *= 0.95
elif season == "Autumn":
    price = 4200
    if number_of_fishermen <= 6:
        price *= 0.90
    if number_of_fishermen > 6 and number_of_fishermen <= 11:
        price *= 0.85
    if number_of_fishermen > 12:
        price *= 0.75
elif season == "Winter":
    price = 2600
    if number_of_fishermen <= 6:
        price *= 0.90
        if number_of_fishermen % 2 == 0:
            price *= 0.95
    if number_of_fishermen > 6 and number_of_fishermen <= 11:
        price *= 0.85
        if number_of_fishermen % 2 == 0:
            price *= 0.95
    if number_of_fishermen > 12:
        price *= 0.75
        if number_of_fishermen % 2 == 0:
            price *= 0.95

if group_budget >= price:
    remaining = group_budget - price
    print(f"Yes! You have {remaining:.2f} USD left.")
else:
    needed = price - group_budget
    print(f"Not enough money! You need {needed:.2f} USD.")