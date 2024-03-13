budget = float(input())
number_of_series = int(input())
counter = 0

while True:
    series = input()
    price = float(input())
    counter += 1
    if series == "Thrones":
        price *= 0.50
    elif series == "Lucifer":
        price *= 0.60
    elif series == "Protector":
        price *= 0.70
    elif series == "TotalDrama":
        price *= 0.80
    elif series == "Area":
        price *= 0.90
    budget -= price
    if number_of_series == counter and budget >= 0:
        print(f"You bought all the series and left with {budget:.2f} USD.")
        break
    elif budget < 0 and number_of_series == counter:
        print(f"You need {abs(budget):.2f} USD. more to buy the series!")
        break