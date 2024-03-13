import math

sum_prime = 0
sum_not_prime = 0

is_prime = True
is_negative = False
number_negative = 0

while True:
    is_prime = True
    number_input = input()

    if number_input == "stop":
        break

    number = int(number_input)

    if number < 0:
        is_negative = True
        number_negative += 1
    else:
        sqrt_num = int(math.sqrt(number))

        for i in range(2,sqrt_num+1):
            if number / i == number//i:
                is_prime = False

        if is_prime and number > 1:
            sum_prime += number
        elif not is_prime or number < 2:
            sum_not_prime += number

if is_negative:
    for n in range(1, number_negative+1):
        print(f"Number is negative.")
print(f"Sum of all prime numbers is: {sum_prime}\nSum of all non prime numbers is: {sum_not_prime}")