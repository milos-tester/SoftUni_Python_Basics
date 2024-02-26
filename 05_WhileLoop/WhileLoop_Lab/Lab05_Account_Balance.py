account_balance = 0

while True:
    inner_input = input()
    if inner_input == "NoMoreMoney":
        break
    elif float(inner_input) < 0:
        print('Invalid operation!')
        break
    else:
        account_balance += float(inner_input)
        print(f'Increase: {float(inner_input):.2f}')
print(f'Total: {account_balance:.2f}')