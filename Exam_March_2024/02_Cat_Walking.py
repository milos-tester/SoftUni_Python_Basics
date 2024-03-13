minutes = int(input())
daily_walks = int(input())
calories = int(input())
total_mins_walk = minutes * daily_walks
total_calories = total_mins_walk * 5
half_calories = calories / 2
if total_calories >= half_calories:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {total_calories}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {total_calories}.")