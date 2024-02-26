width = int(input())
length = int(input())
height = int(input())
cubic_space = width * length * height
while True:
    boxes_input = input()
    if boxes_input == "Done":
        print(f"{cubic_space} Cubic meters left.")
        break
    cubic_space -= int(boxes_input)
    if cubic_space < 0:
        print(f"No more free space! You need {-cubic_space} Cubic meters more.")
        break