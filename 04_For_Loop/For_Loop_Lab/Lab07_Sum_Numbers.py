numbers_count = int(input())

result = 0

for i in range(0, numbers_count):
    inner_input = int(input())
    result += inner_input

print(result)