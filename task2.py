def calculate_bill(units):

    if units <= 100:
        energy_charge = units * 2
    elif units <= 200:
        energy_charge = (100 * 2) + (units - 100) * 3
    elif units <= 300:
        energy_charge = (100 * 2) + (100 * 3) + (units - 200) * 5
    else:
        energy_charge = (100 * 2) + (100 * 3) + (100 * 5) + (units - 300) * 7

    fixed_charge = 50
    surcharge = energy_charge * 0.05


    rebate = 20 if units <= 100 else 0

    total_bill = energy_charge + fixed_charge + surcharge - rebate

    return round(total_bill, 2)



months = ["January", "February", "March", "April", "May", "June"]
bills = []

print("PROGRESSIVE ELECTRICITY BILLING SYSTEM")

for month in months:
    units = int(input(f"Enter units consumed in {month}: "))
    bill = calculate_bill(units)
    bills.append(bill)

    print(f"{month} Electricity Bill: Rs.{bill:.2f}")


print("\nMONTHLY BILL COMPARISON")

for i in range(len(bills)):
    if i > 0:
        increase = bills[i] - bills[i - 1]
        percentage = (increase / bills[i - 1]) * 100

        print(f"{months[i]}: Change = Rs.{increase:.2f}")

        if percentage > 30:
            print("Warning: Unusual increase in electricity bill!")

print("\nHighest Bill: Rs.", max(bills))
print("Lowest Bill: Rs.", min(bills))
print("Average Bill: Rs.", round(sum(bills) / len(bills), 2))
