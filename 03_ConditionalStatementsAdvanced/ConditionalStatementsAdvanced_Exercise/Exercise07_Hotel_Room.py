month = input()
nights = int(input())

if month == "May" or month == "October":
    apartment_price = nights * 65.00
    studio_price = nights * 50.00
    if nights > 7 and nights <= 14:
        studio_price *= 0.95
    elif nights > 14:
        studio_price *= 0.70
        apartment_price *= 0.90
elif month == "June" or month == "September":
    apartment_price = nights * 68.70
    studio_price = nights * 75.20
    if nights > 14:
        studio_price *= 0.80
        apartment_price *= 0.90
elif month == "July" or month == "August":
    apartment_price = nights * 77.00
    studio_price = nights * 76.00
    if nights > 14:
        apartment_price *= 0.90

print(f"Apartment: {apartment_price:.2f} USD.\nStudio: {studio_price:.2f} USD.")