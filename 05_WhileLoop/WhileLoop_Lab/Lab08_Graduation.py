student_name = input()

sum_grades = 0
counter_grade = 0
counter_failed_grade = 0

while True:
    inner_input = float(input())
    if inner_input < 4.00:
        counter_failed_grade += 1
    else:
        sum_grades += inner_input
        counter_grade += 1

    if counter_failed_grade == 2:
        print(f'{student_name} has been excluded at {counter_grade+1} grade')
        break

    if counter_grade == 12:
        break

if counter_grade == 12:
    print(f'{student_name} graduated. Average grade: {(sum_grades/12):.2f}')