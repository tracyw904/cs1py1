price = float(input("enter your price values: "))


discount = 0

if price >=50:
    discount = (price*.1)
elif price>=25:
        discount = price*.05
else:
        price = price - discount

print("Your actual price is " + str(price))