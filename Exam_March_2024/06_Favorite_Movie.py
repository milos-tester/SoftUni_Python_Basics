import sys
top_score = -sys.maxsize
counter = 0
best_movie = ""
while True:
    input_movie = input()
    counter += 1
    result = 0
    if input_movie == "STOP":
        break
    for char in input_movie:
        if char.islower():
            result += ord(char) - 2 * len(input_movie)
        elif char.isupper():
            result += ord(char) - len(input_movie)
        else:
            result += ord(char)
    if result > top_score:
        top_score = result
        best_movie = input_movie
    if counter == 7:
        print(f"The limit is reached.")
        break
print(f"The best movie for you is {best_movie} with {top_score} ASCII sum.")
