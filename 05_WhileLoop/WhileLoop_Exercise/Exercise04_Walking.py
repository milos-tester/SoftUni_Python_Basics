walking_sum = 0

while True:
    walking_input = input()
    if walking_input == "Going home":
        walking_sum += int(input())
        if walking_sum >= 10000:
            print(f"Goal reached! Good job!\n{walking_sum - 10000} steps over the goal!")
            break
        else:
            print(f"{10000-walking_sum} more steps to reach goal.")
            break
    walking_sum += int(walking_input)
    if walking_sum >= 10000:
        print(f"Goal reached! Good job!\n{walking_sum-10000} steps over the goal!")
        break