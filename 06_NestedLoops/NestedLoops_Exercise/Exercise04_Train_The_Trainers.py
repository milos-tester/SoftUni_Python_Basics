n = int(input())
result = 0
final_result = 0
counter = 0

while True:
    result = 0
    inner_input = input()
    if inner_input == "Finish":
        break
    for i in range(0, n):
        number_input = float(input())
        result += number_input
        counter += 1
    print(f"{inner_input} - {(result/n):.2f}.")
    final_result += result

print(f"Student's final assessment is {(final_result/counter):.2f}.")