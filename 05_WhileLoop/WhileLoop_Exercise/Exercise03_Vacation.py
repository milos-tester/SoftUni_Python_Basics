vacation_money = float(input())
available_money = float(input())
spend_counter = 0
day_counter = 0

while True:
    type_input = input()
    money_input = float(input())
    day_counter += 1

    if type_input == "spend":
        spend_counter += 1
        available_money -= money_input
        if available_money < 0:
            available_money = 0
    elif type_input == "save":
        spend_counter = 0
        available_money += money_input

    if spend_counter == 5:
        print(f"You can't save the money.\n{day_counter}")
        break

    if available_money >= vacation_money:
        print(f"You saved the money for {day_counter} days.")
        break
