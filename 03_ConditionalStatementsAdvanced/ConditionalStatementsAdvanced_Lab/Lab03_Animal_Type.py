animal_input = input()

if animal_input == "dog":
    print('mammal')
elif animal_input == "crocodile" or animal_input == "tortoise" or animal_input == "snake":
    print('reptile')
else:
    print('unknown')