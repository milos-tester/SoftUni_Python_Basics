hours_input = int(input())
minutes_input = int(input())

total_minutes = hours_input * 60 + minutes_input + 15

result_hours = total_minutes // 60
result_minutes = total_minutes % 60

if result_hours == 24:
    result_hours = 0

if result_minutes < 10:
    print(f'{result_hours}:0{result_minutes}')
else:
    print(f'{result_hours}:{result_minutes}')