start_number = int(input())
end_number = int(input())
magic_number = int(input())

counter = 0
inner_counter = 0

for i in range (start_number, end_number+1):
    for j in range (start_number, end_number+1):
        counter += 1
        if i + j == magic_number:
            inner_counter += 1
            if inner_counter == 1:
                print(f"Combination N:{counter} ({i} + {j} = {magic_number})")

if inner_counter < 1:
    print(f"{counter} combinations - neither equals {magic_number}")

