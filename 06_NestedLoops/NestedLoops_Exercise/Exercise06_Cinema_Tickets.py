counter = 0
student_counter = 0
standard_counter = 0
kids_counter = 0

while True:
    movie_input = input()
    if movie_input == "Finish":
        break
    seats_number = int(input())
    seats_holder = seats_number
    counter = 0
    while True:
        ticket_input = input()
        if ticket_input == "End":
            break
        elif ticket_input == "student":
            student_counter += 1
        elif ticket_input == "standard":
            standard_counter += 1
        elif ticket_input == "kid":
            kids_counter += 1
        counter += 1
        seats_number -= 1
        if seats_number == 0:
            break
    print(f"{movie_input} - {counter/seats_holder*100:.2f}% full.")

result = student_counter + standard_counter + kids_counter
students = student_counter / result * 100
standard = standard_counter / result * 100
kids = kids_counter / result * 100
print(f"Total tickets: {result}\n{students:.2f}% student tickets.\n{standard:.2f}% standard tickets.\n{kids:.2f}% kids tickets.")