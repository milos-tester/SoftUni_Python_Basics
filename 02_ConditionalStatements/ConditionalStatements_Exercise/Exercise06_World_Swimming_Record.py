record_in_seconds = float(input())
distance_in_meters = float(input())
time_for_one_meter = float(input())

total_time = distance_in_meters * time_for_one_meter
added_time = (distance_in_meters // 15) * 12.5
final_time = total_time + added_time

if final_time < record_in_seconds:
    print(f'Yes, he succeeded! The new world record is {final_time:.2f} seconds.')
else:
    print(f'No, he failed! He was {(final_time-record_in_seconds):.2f} seconds slower.')