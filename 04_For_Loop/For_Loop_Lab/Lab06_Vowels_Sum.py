textInput = input()

result = 0

for i in textInput:
    if i == "a":
        result += 1
    elif i == "e":
        result += 2
    elif i == "i":
        result += 3
    elif i == "o":
        result += 4
    elif i == "u":
        result += 5

print(result)