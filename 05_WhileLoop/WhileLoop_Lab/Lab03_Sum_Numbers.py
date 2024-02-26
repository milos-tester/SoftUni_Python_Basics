number_input = int(input())
sum_result = 0

while True:
    inner_input = int(input())
    sum_result += inner_input
    if sum_result >= number_input:
        break
print(sum_result)