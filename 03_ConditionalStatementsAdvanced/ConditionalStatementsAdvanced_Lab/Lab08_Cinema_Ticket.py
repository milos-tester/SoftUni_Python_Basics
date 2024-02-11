day_input = input()

if day_input == "Monday" or day_input == "Tuesday" or day_input == "Friday":
    print("12")
elif day_input == "Wednesday" or day_input == "Thursday":
    print("14")
elif day_input == "Saturday" or day_input == "Sunday":
    print("16")