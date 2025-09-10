def discount(price, category):
    if category == "student":
        discount_rate = 0.9 if price > 1000 else 0.95
    elif category == "regular" and price > 2000:
        discount_rate = 0.85
    else:
        discount_rate = 1.0
    return price * discount_rate

print(discount(1200, "student"))
print(discount(900, "student"))
print(discount(2500, "regular"))
print(discount(1500, "regular"))