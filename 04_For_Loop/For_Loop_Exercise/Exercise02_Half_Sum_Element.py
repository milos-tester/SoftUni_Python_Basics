import sys

count_numbers = int(input())

max_number = -sys.maxsize
result_sum = 0

for i in range(0, count_numbers):
    inner_input = int(input())
    if inner_input > max_number:
        max_number = inner_input

    result_sum += inner_input

if max_number == result_sum - max_number:
    print(f'Yes\nSum = {result_sum-max_number}')
else:
    sum_numbers = result_sum - max_number
    diff = abs(max_number - sum_numbers)
    print(f'No\nDiff = {diff}')