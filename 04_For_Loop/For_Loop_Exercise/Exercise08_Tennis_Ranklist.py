tournaments_number = int(input())
initial_points = int(input())
tournament_points = 0
won_count = 0

for i in range (0, tournaments_number):
    tournament_stage = input()
    if tournament_stage == "W":
        initial_points += 2000
        tournament_points += 2000
        won_count += 1
    elif tournament_stage == "F":
        initial_points += 1200
        tournament_points += 1200
    elif tournament_stage == "SF":
        initial_points += 720
        tournament_points += 720

won_result = won_count / tournaments_number * 100
average = tournament_points // tournaments_number
print(f'Final points: {initial_points}\nAverage points: {average}\n{won_result:.2f}%')