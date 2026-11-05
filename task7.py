
n = int(input("Enter number of products: "))
total = 0

for i in range(n):
    print("\nProduct", i + 1)

    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    qty = int(input("Enter quantity: "))
    category = input("Enter category (food/electronics): ").lower()

    amount = price * qty

    if category == "food":
        tax = amount * 0.05
    else:
        tax = amount * 0.18

    total = total + amount + tax

    print("Product:", name)
    print("Amount: Rs.", amount)
    print("Tax: Rs.", round(tax, 2))

if total >= 5000:
    discount = total * 0.15
elif total >= 2000:
    discount = total * 0.10
else:
    discount = total * 0.05

if discount > 1000:
    discount = 1000

final_bill = total - discount

print("\n========== FINAL INVOICE ==========")
print("Total Amount: Rs.", round(total, 2))
print("Discount: Rs.", round(discount, 2))
print("Final Bill: Rs.", round(final_bill, 2))
print("===================================")
