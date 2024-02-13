type_of_flowers = input()
number_of_flowers = int(input())
budget = int(input())

price = 0

if type_of_flowers == "Roses":
    price = number_of_flowers * 5.00
    if number_of_flowers > 80:
        price *= 0.90
elif type_of_flowers == "Dahlias":
    price = number_of_flowers * 3.80
    if number_of_flowers > 90:
        price *= 0.85
elif type_of_flowers == "Tulips":
    price = number_of_flowers * 2.80
    if number_of_flowers > 80:
        price *= 0.85
elif type_of_flowers == "Narcissus":
    price = number_of_flowers * 3.00
    if number_of_flowers < 120:
        price *= 1.15
elif type_of_flowers == "Gladiolus":
    price = number_of_flowers * 2.50
    if number_of_flowers < 80:
        price *= 1.20

if budget >= price:
    remaining = budget - price
    print(f"Hey, you have a great garden with {number_of_flowers} {type_of_flowers} and {remaining:.2f} USD left.")
else:
    needed = price - budget
    print(f"Not enough money, you need {needed:.2f} USD more.")