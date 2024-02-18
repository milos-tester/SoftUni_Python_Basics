import sys

numbers_count = int(input())

min_number = sys.maxsize
max_number = -sys.maxsize

for i in range (0, numbers_count):
    inner_input = int(input())
    if inner_input < min_number:
        min_number = inner_input
    if inner_input > max_number:
        max_number = inner_input

print(f'Max number: {max_number}')
print(f'Min number: {min_number}')