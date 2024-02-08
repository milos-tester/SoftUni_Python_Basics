number_of_pages = int(input())
pages_per_hour = int(input())
number_of_days_to_finish_book = int(input())
total_time = number_of_pages // pages_per_hour
required_hours_per_day = total_time // number_of_days_to_finish_book
print(required_hours_per_day)