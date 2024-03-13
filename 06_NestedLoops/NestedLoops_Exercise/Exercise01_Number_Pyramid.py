number = int(input())
counter = 1
checker = False
for i in range(1, number+1):
    for j in range(1, i+1):
        if counter > number:
            checker = True
            break
        print(str(counter) + " ", end="")
        counter += 1
    if checker:
        break
    print()