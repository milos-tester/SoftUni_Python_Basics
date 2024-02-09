import math

series = str(input())
episode_dur = int(input())
break_time = int(input())

lunchtime = break_time / 8
rest_time = break_time / 4
left_time = break_time - lunchtime - rest_time

if episode_dur <= left_time:
    more_time = math.ceil(left_time - episode_dur)
    print(f"You have enough time to watch {series} and left with {more_time} minutes free time.")
else:
    need_more = math.ceil(episode_dur - left_time)
    print(f"You don't have enough time to watch {series}, you need {need_more} more minutes.")