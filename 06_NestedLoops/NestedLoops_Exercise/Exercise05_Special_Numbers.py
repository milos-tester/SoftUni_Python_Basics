number = int(input())

checker = True

for i in range(1111, 9999):
    number_string = str(i)
    for index, digit in enumerate(number_string):
        digit = int(digit)

        if digit != 0 and number % digit == 0:
            checker = True
        else:
            checker = False
            break
    if checker:
        print(str(i), end=" ")