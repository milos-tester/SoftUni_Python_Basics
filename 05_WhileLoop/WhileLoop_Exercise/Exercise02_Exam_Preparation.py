poor_grades_number = int(input())
poor_grades_counter = 0
problem_counter = 0
average_score = 0
sum_grades = 0
grade_input = 0
problem_name = ""

while True:
    problem_input = str(input())

    if problem_input == "Enough":
        print(f'Average score: {(sum_grades/problem_counter):.2f}\nNumber of problems: {problem_counter}\nLast problem: {problem_name}')
        break
    problem_name = problem_input
    grade_input = int(input())
    sum_grades += grade_input
    problem_counter += 1
    if grade_input <= 4:
        poor_grades_counter += 1

    if poor_grades_number == poor_grades_counter:
        print(f'You need a break, {poor_grades_counter} poor grades.')
        break
