package_of_pens = int(input())
package_of_markers = int(input())
liters_of_detergent = int(input())
precentage_reduction = int(input())
pens_price = 5.80
markers_price = 7.20
detergent_price = 1.20
price_of_all_products = package_of_pens * pens_price + package_of_markers * markers_price + liters_of_detergent * detergent_price
final_price = price_of_all_products - (price_of_all_products * precentage_reduction / 100)
print(final_price)