budget = float(input())
num_video_cards = int(input())
num_cpu = int(input())
num_ram = int(input())

sum_video_cards = num_video_cards * 250
sum_cpu = num_cpu * sum_video_cards * 0.35
sum_ram = num_ram * sum_video_cards * 0.10

total_sum = sum_video_cards + sum_cpu + sum_ram

if num_video_cards > num_cpu:
    total_sum = total_sum * 0.85

if budget>=total_sum:
    print(f'You have {(budget-total_sum):.2f} USD left!')
else:
    print(f'Not enough money! You need {(total_sum-budget):.2f} USD more!')
