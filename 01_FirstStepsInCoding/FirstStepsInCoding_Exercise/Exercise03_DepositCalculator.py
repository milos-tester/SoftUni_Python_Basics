deposit = float(input())
term_of_deposit = int(input())
anual_interest_rate = float(input())

interest = deposit * (anual_interest_rate / 100)
interest_one_month = interest / 12
amount = deposit + (term_of_deposit * interest_one_month)
print(amount)