amount_of_nylon = int(input())
amount_of_paint = int(input())
amount_of_detergent = int(input())
hours = int(input())
nylon_price = 1.50
paint_price = 14.50
paint_thinner_price = 5.00
bags_price = 0.40
sum_for_nylon = (amount_of_nylon + 2) * nylon_price
sum_for_paint = (amount_of_paint * 1.10) * paint_price
sum_for_detergent = amount_of_detergent * paint_thinner_price
total_sum_materials = sum_for_nylon + sum_for_paint + sum_for_detergent + bags_price
sum_for_workers = (total_sum_materials * 0.30) * hours
total_sum = total_sum_materials + sum_for_workers
print(total_sum)