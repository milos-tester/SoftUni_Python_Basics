furit = input()
size = input()
sets = int(input())
price = 0

if furit == "Watermelon":
    if size == "small":
        price = 2 * 56.00
    elif size == "big":
        price = 5 * 28.70
elif furit == "Mango":
    if size == "small":
        price = 2 * 36.66
    elif size == "big":
        price = 5 * 19.60
elif furit == "Pineapple":
    if size == "small":
        price = 2 * 42.10
    elif size == "big":
        price = 5 * 24.80
elif furit == "Raspberry":
    if size == "small":
        price = 2 * 20.00
    elif size == "big":
        price = 5 * 15.20

total_price = price * sets

if total_price >= 400 and total_price <= 1000:
    total_price *= 0.85
elif total_price > 1000:
    total_price *= 0.50

print(f"{total_price:.2f} USD.")