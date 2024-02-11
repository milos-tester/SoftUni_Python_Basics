hour_input = int(input())
day_input = input()

if hour_input >= 10 and hour_input <= 18:
    if day_input != "Sunday":
        print('open')
    else:
        print('closed')
else:
    print('closed')