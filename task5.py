
data_needed = float(input("Enter required data (GB): "))
validity_needed = int(input("Enter required validity (days): "))
budget = float(input("Enter your budget (Rs.): "))

plans = [
    ["Plan A", 199, 2, 28, 50],
    ["Plan B", 299, 3, 56, 40],
    ["Plan C", 399, 5, 84, 30],
    ["Plan D", 499, 10, 84, 20]
]

eligible = []

print("\n========== PLAN COMPARISON ==========")

for plan in plans:
    name, price, data, validity, extra_charge = plan

    excess_data = max(0, data_needed - data)
    excess_cost = excess_data * extra_charge
    total_cost = price + excess_cost

    print("\nPlan:", name)
    print("Base Price: Rs.", price)
    print("Excess Charges: Rs.", excess_cost)
    print("Total Cost: Rs.", total_cost)

    if validity >= validity_needed and total_cost <= budget:
        eligible.append([name, total_cost])

print("\n========== RESULT ==========")

if eligible:
    best_plan = min(eligible, key=lambda x: x[1])
    print("Most Economical Plan:", best_plan[0])
    print("Total Cost: Rs.", best_plan[1])
else:
    print("No eligible plan found within your budget.")

