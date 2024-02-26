import sys

max_number = -sys.maxsize

while True:
    inner_input = input()
    if inner_input == "Stop":
        break
    elif int(inner_input) > max_number:
        max_number = int(inner_input)

print(max_number)