groups_number = int(input())
makalu_count = 0
mont_blanc_count = 0
kilimanjaro_count = 0
k2_count = 0
everest_count = 0
total_climbers = 0

for i in range(0, groups_number):
    climbers_number = int(input())
    total_climbers += climbers_number
    if climbers_number <= 5:
        makalu_count += climbers_number
    elif climbers_number > 5 and climbers_number <= 12:
        mont_blanc_count += climbers_number
    elif climbers_number > 12 and climbers_number <= 25:
        kilimanjaro_count += climbers_number
    elif climbers_number > 25 and climbers_number <= 40:
        k2_count += climbers_number
    elif climbers_number > 40:
        everest_count += climbers_number

result_makalu = makalu_count / total_climbers * 100
result_mont_blanc = mont_blanc_count / total_climbers * 100
result_kilimanjaro = kilimanjaro_count / total_climbers * 100
result_k2 = k2_count / total_climbers * 100
result_everest = everest_count / total_climbers * 100

print(f'{result_makalu:.2f}%\n{result_mont_blanc:.2f}%\n{result_kilimanjaro:.2f}%\n{result_k2:.2f}%\n{result_everest:.2f}%')