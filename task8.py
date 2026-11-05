
product = input("Enter product name: ")
quantity = int(input("Enter quantity produced: "))

material = float(input("Enter material cost: "))
labour = float(input("Enter labour charges: "))
machine = float(input("Enter machine cost: "))
wastage = float(input("Enter wastage cost: "))
selling_price = float(input("Enter selling price per unit: "))
target = float(input("Enter profit target: "))

total_cost = material + labour + machine + wastage

revenue = quantity * selling_price
profit = revenue - total_cost

print("\n======= PRODUCTION REPORT =======")
print("Product:", product)
print("Quantity:", quantity)
print("Material Cost: Rs.", material)
print("Labour Cost: Rs.", labour)
print("Machine Cost: Rs.", machine)
print("Wastage Cost: Rs.", wastage)
print("Total Cost: Rs.", total_cost)
print("Total Revenue: Rs.", revenue)
print("Profit: Rs.", profit)

if profit >= target:
    print("Profit Target Achieved!")
else:
    print("Profit Target Not Achieved!")

print("=================================")
