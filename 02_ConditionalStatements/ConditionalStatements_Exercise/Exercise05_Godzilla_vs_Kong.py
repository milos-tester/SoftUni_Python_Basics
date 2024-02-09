movie_budget = float(input())
number_of_extras = int(input())
price_for_clothing = float(input())

sum_for_decor = movie_budget * 0.10
sum_for_clothes = number_of_extras * price_for_clothing


if number_of_extras > 150:
    sum_for_clothes = sum_for_clothes * 0.90

total_sum = sum_for_clothes + sum_for_decor

remaining_money = movie_budget - total_sum
needed_money = total_sum - movie_budget

if total_sum > movie_budget:
    print(f'Not enough money!\nWingard needs {needed_money:.2f} USD more.')
else:
    print(f'Action!\nWingard starts filming with {remaining_money:.2f} USD left.')
