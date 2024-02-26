import sys

min_number = sys.maxsize

while True:
    inner_input = input()
    if inner_input == "Stop":
        break
    elif int(inner_input) < min_number:
        min_number = int(inner_input)

print(min_number)