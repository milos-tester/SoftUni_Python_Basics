budget = float(input())
season = input()

holiday = ""
destination = ""

if budget <= 100:
    if season == "summer":
        destination = "Serbia"
        holiday = "Camp"
        budget *= 0.30
    elif season == "winter":
        destination = "Serbia"
        holiday = "Hotel"
        budget *= 0.70
elif budget > 100 and budget <= 1000:
    if season == "summer":
        destination = "Balkans"
        holiday = "Camp"
        budget *= 0.40
    elif season == "winter":
        destination = "Balkans"
        holiday = "Hotel"
        budget *= 0.80
elif budget > 1000:
    destination = "Europe"
    holiday = "Hotel"
    budget *= 0.90

print(f"Somewhere in {destination}\n{holiday} - {budget:.2f}")