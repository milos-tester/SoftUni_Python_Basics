book_to_find = input()

book_counter = 0

while True:
    inner_input = input()

    if inner_input == "No More Books":
        print(f"The book you search is not here!\nYou checked {book_counter} books.")
        break
    elif inner_input == book_to_find:
        print(f'You checked {book_counter} books and found it.')
        break
    book_counter += 1