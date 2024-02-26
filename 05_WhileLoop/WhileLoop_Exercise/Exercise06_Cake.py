cake_width = int(input())
cake_length = int(input())

cake_dimension = cake_width * cake_length

while True:
    piece_input = input()
    if piece_input == "STOP":
        print(f"{cake_dimension} pieces are left.")
        break
    cake_dimension -= int(piece_input)

    if cake_dimension < 0:
        print(f"No more cake left! You need {-cake_dimension} pieces more.")
        break