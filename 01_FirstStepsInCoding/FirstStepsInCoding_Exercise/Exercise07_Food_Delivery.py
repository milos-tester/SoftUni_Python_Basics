chicken_menu_number = int(input())
fish_menu_number = int(input())
vegetarian_menu_number = int(input())
total_price =chicken_menu_number * 10.35 + fish_menu_number * 12.40 + vegetarian_menu_number * 8.15
desert_price = total_price * 0.20
final_price = total_price + desert_price + 2.50
print(final_price)