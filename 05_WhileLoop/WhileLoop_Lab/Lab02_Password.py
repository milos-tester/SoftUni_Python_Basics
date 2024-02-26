username = input()
password = input()

while True:
    data_input = input()
    if data_input == password:
        break
print(f'Welcome, {username}!')