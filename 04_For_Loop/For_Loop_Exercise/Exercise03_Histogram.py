number_count = int(input())

range_one = 0
range_two = 0
range_three = 0
range_four = 0
range_five = 0

for i in range(0, number_count):
    inner_input = int(input())
    if inner_input < 200:
        range_one += 1
    elif inner_input >= 200 and inner_input <= 399:
        range_two += 1
    elif inner_input > 399 and inner_input <= 599:
        range_three += 1
    elif inner_input > 599 and inner_input <= 799:
        range_four += 1
    elif inner_input > 799:
        range_five +=1

result_one = range_one / number_count * 100
result_two = range_two / number_count * 100
result_three = range_three / number_count * 100
result_four = range_four / number_count * 100
result_five = range_five / number_count * 100

print(f'{result_one:.2f}%\n{result_two:.2f}%\n{result_three:.2f}%\n{result_four:.2f}%\n{result_five:.2f}%')
