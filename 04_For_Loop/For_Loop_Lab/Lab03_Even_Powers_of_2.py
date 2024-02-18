import math

inputNumber = int(input())

for number in range(0, inputNumber + 1):
    if number % 2 == 0:
        print(int(math.pow(2, number)))