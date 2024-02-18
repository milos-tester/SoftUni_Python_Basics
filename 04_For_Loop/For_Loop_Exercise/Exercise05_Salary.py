number_of_tabs = int(input())
salary = int(input())

for i in range(0, number_of_tabs):
    site_input = input()
    if site_input == "Facebook":
        salary -= 150
    elif site_input == "Instagram":
        salary -= 100
    elif site_input == "Reddit":
        salary -= 50

    if salary <= 0:
        print(f'You have lost your salary.')
        break

if salary > 0:
    print(salary)