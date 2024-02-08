puzzle = 2.60
talking_doll = 3.00
teddy_bear = 4.10
minion = 8.20
truck = 2.00

price_of_the_trip = float(input())
num_puzzles = int(input())
num_talking_dolls = int(input())
num_teddy_bears = int(input())
num_minions = int(input())
num_trucks = int(input())

toys_price = ((puzzle * num_puzzles) + (talking_doll * num_talking_dolls) + (teddy_bear * num_teddy_bears)
              + (minion * num_minions) + (truck * num_trucks))
num_toys = puzzle + talking_doll + teddy_bear + minion + truck

profit = toys_price - (toys_price*0.10)