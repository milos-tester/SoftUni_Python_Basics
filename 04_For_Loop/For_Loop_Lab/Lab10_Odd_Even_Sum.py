input_number = int(input())

sum_odd = 0
sum_even = 0

for i in range(0, input_number):
    inner_input = int(input())
    if i % 2 == 0:
        sum_even += inner_input
    else:
        sum_odd += inner_input

if sum_odd == sum_even:
    print(f'Yes\nSum = {sum_odd}')
else:
    diff = abs(sum_odd - sum_even)
    print(f'No\nDiff = {diff}')