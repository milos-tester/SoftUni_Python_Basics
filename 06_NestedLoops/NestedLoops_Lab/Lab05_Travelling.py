while True:
    destination = input()
    if destination == "End":
        break
    money = float(input())
    while True:
        money -= float(input())
        if money <= 0:
            print(f"Going to {destination}!")
            break