first_number = int(input())
second_number = int(input())
string_number = ""


for i in range(first_number, second_number+1):
    string_number = str(i)
    odd_sum = 0
    even_sum = 0
    for index, digit in enumerate(string_number):
        if index % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)
    if even_sum == odd_sum:
        print(i, end=" ")