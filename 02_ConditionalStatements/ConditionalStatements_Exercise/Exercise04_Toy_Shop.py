price_of_the_trip = float(input())
num_puzzles = int(input())
num_talking_dolls = int(input())
num_teddy_bears = int(input())
num_minions = int(input())
num_trucks = int(input())

puzzle = 2.60
talking_doll = 3.00
teddy_bear = 4.10
minion = 8.20
truck = 2.00

toys_price = ((puzzle * num_puzzles) + (talking_doll * num_talking_dolls) + (teddy_bear * num_teddy_bears)
              + (minion * num_minions) + (truck * num_trucks))

num_toys = num_puzzles + num_talking_dolls + num_teddy_bears + num_minions + num_trucks
if num_toys >= 50:
    toys_price = toys_price * 0.75

rent = toys_price * 0.10
profit = toys_price - rent
remaining = profit - price_of_the_trip
needed_money = price_of_the_trip - profit
if profit >= price_of_the_trip:
    print(f'Yes! {remaining:.2f} USD left.')
else:
    print(f'Not enough money! {needed_money:.2f} USD needed.')