price_list = {
    "apple": 12.99,
    "orange": 14.99,
    "cherry": 26.25,
}

# product  ->  quantity
cart = {}

cart["orange"] = 0
cart["cherry"] = 0


print(cart)

if "apple" not in cart.keys():
    cart["apple"] = 0

cart["apple"] += 1


print(cart)
print("#" * 30)
a = [1, 2]
for key, value in cart.items():
    if value == 0:
        del cart[key]

print(cart)
