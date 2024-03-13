import math

tennis_racket = float(input())
rackets_number = int(input())
sneakers = int(input())

price_rackets = tennis_racket * rackets_number
price_sneakers = tennis_racket / 6
price_all_sneakers = price_sneakers * sneakers
price_equipment = (price_rackets + price_all_sneakers) * 0.20
total_price = price_rackets + price_all_sneakers + price_equipment
print(f"Price to be paid by Djokovic {math.floor(total_price/8)}")
print(f"Price to be paid by sponsors {math.ceil(total_price*7/8) }")