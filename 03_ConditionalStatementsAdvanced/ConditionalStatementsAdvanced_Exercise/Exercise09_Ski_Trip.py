days_of_stay = int(input())
room_type = input()
grade = input()

nights = days_of_stay - 1
price = 0.00

if room_type == "room for one person":
    price = 18.00 * nights
elif room_type == "apartment":
    price = 25.00 * nights
    if days_of_stay < 10:
        price *= 0.70
    elif days_of_stay >= 10 and days_of_stay <= 15:
        price *= 0.65
    elif days_of_stay > 15:
        price *= 0.50
elif room_type == "president apartment":
    price = 35.00 * nights
    if days_of_stay < 10:
        price *= 0.90
    elif days_of_stay >= 10 and days_of_stay <= 15:
        price *= 0.85
    elif days_of_stay > 15:
        price *= 0.80
if grade == "positive":
    price *= 1.25
elif grade == "negative":
    price *= 0.90

print(f"{price:.2f}")
