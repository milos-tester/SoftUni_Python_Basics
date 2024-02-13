degrees = int(input())
time_of_the_day = input()

clothing = ""
shoes = ""

if degrees >= 10 and degrees <= 18:
    if time_of_the_day == "Morning":
        clothing = "Sweatshirt"
        shoes = "Sneakers"
    elif time_of_the_day == "Afternoon":
        clothing = "Shirt"
        shoes = "Moccasins"
    elif time_of_the_day == "Evening":
        clothing = "Shirt"
        shoes = "Moccasins"
elif degrees > 18 and degrees <= 24:
    if time_of_the_day == "Morning":
        clothing = "Shirt"
        shoes = "Moccasins"
    elif time_of_the_day == "Afternoon":
        clothing = "T-Shirt"
        shoes = "Sandals"
    elif time_of_the_day == "Evening":
        clothing = "Shirt"
        shoes = "Moccasins"
elif degrees >= 25:
    if time_of_the_day == "Morning":
        clothing = "T-Shirt"
        shoes = "Sandals"
    elif time_of_the_day == "Afternoon":
        clothing = "Swim Suit"
        shoes = "Barefoot"
    elif time_of_the_day == "Evening":
        clothing = "Shirt"
        shoes = "Moccasins"

print(f"It's {degrees} degrees, get your {clothing} and {shoes}.")