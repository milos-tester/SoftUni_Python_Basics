city_name = input()
sales_volume = float(input())

if city_name == "London":
    if 0 <= sales_volume <= 500:
        sales_volume = sales_volume * 0.05
        print(f'{sales_volume:.2f}')
    elif 500 < sales_volume <= 1000:
        sales_volume = sales_volume * 0.07
        print(f'{sales_volume:.2f}')
    elif 1000 < sales_volume <= 10000:
        sales_volume = sales_volume * 0.08
        print(f'{sales_volume:.2f}')
    elif sales_volume > 10000:
        sales_volume = sales_volume * 0.12
        print(f'{sales_volume:.2f}')
    else:
        print('error')
elif city_name == "Paris":
    if 0 <= sales_volume <= 500:
        sales_volume = sales_volume * 0.045
        print(f'{sales_volume:.2f}')
    elif 500 < sales_volume <= 1000:
        sales_volume = sales_volume * 0.075
        print(f'{sales_volume:.2f}')
    elif 1000 < sales_volume <= 10000:
        sales_volume = sales_volume * 0.10
        print(f'{sales_volume:.2f}')
    elif sales_volume > 10000:
        sales_volume = sales_volume * 0.13
        print(f'{sales_volume:.2f}')
    else:
        print('error')
elif city_name == "Rome":
    if 0 <= sales_volume <= 500:
        sales_volume = sales_volume * 0.055
        print(f'{sales_volume:.2f}')
    elif 500 < sales_volume <= 1000:
        sales_volume = sales_volume * 0.08
        print(f'{sales_volume:.2f}')
    elif 1000 < sales_volume <= 10000:
        sales_volume = sales_volume * 0.12
        print(f'{sales_volume:.2f}')
    elif sales_volume > 10000:
        sales_volume = sales_volume * 0.145
        print(f'{sales_volume:.2f}')
    else:
        print('error')
else:
    print('error')