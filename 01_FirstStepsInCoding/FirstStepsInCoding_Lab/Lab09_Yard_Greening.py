squareMetersInput = float(input())
pricePerSquareMeter = 7.61
priceForWholeYard = squareMetersInput * pricePerSquareMeter
discountValue = priceForWholeYard * 0.18
result = priceForWholeYard - discountValue
print(f'The final price is: {result} USD.\nThe discount is: {discountValue} USD.')