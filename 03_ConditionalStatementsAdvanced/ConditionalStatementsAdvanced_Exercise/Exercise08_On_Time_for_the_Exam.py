exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minut = int(input())

exam_time = exam_hour * 60 + exam_minute
arrival_time = arrival_hour * 60 + arrival_minut

if arrival_time == exam_time:
    print("On time")
elif arrival_time < exam_time:
    difference = exam_time - arrival_time
    if difference == 0:
        print(f"On time")
    elif difference <= 30:
        print(f"On time\n{difference} minutes before the start")
    elif difference > 30 and difference < 60:
        print(f"Early\n{difference} minutes before the start")
    elif difference >= 60:
        hours_difference = difference // 60
        minutes_difference = difference % 60
        if minutes_difference < 10:
            print(f"Early\n{hours_difference}:0{minutes_difference} hours before the start")
        else:
            print(f"Early\n{hours_difference}:{minutes_difference} hours before the start")
else:
    difference = arrival_time - exam_time
    if difference < 60:
        print(f"Late\n{difference} minutes after the start")
    else:
        hours_difference = difference // 60
        minutes_difference = difference % 60
        if minutes_difference < 10:
            print(f"Late\n{hours_difference}:0{minutes_difference} hours after the start")
        else:
            print(f"Late\n{hours_difference}:{minutes_difference} hours after the start")