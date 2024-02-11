age_input = float(input())
gender_input = input()
if gender_input == "m":
    if age_input >= 16:
        print('Mr.')
    else:
        print('Master')
elif gender_input == "f":
    if age_input >= 16:
        print('Ms.')
    else:
        print('Miss')