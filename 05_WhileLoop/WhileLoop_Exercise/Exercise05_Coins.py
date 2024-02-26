#The coins can be 2.00 EUR, 1.00 EUR, 0.50 EUR, 0.20 EUR, 0.10 EUR, 0.05 EUR, 0.02 EUR, 0.01 EUR.

money_input = float(input())
change = int(money_input*100)
counter = 0

while True:
    if change >= 200:
        change -= 200
    elif change >= 100:
        change -= 100
    elif change >= 50:
        change -= 50
    elif change >= 20:
        change -= 20
    elif change >= 10:
        change -= 10
    elif change >= 5:
        change -= 5
    elif change >= 2:
        change -= 2
    elif change >= 1:
        change -= 1
    counter += 1
    if change == 0:
        break
print(counter)