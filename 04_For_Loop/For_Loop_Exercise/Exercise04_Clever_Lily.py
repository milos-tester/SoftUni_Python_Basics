lily_age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

money_count = 0
toy_count = 0
brother_count = 0

for i in range(1, lily_age+1):
    if i % 2 == 0:
        money_count += 10 * i/2
        brother_count += 1
    else:
        toy_count += 1

sell_toys = toy_count * toy_price
total_result = (money_count + sell_toys) - brother_count

if total_result >= washing_machine_price:
    print(f'Yes! {total_result-washing_machine_price:.2f}')
else:
    print(f'No! {washing_machine_price-total_result:.2f}')