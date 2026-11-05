
distance = int(input("Enter distance in km: "))
n = int(input("Enter number of passengers: "))
total = 0

for i in range(n):
    print("\nPassenger", i + 1)
    age = int(input("Enter age: "))
    cls = input("Enter class (Sleeper/AC): ").lower()

    if distance <= 100:
        rate = 1
    elif distance <= 500:
        rate = 1.5
    else:
        rate = 2


    if cls == "ac":
        rate = rate * 2
        fee = 50
    else:
        fee = 20

    fare = distance * rate

    if age < 5:
        fare = 0
        fee = 0
    elif age >= 60:
        fare = fare * 0.8

    amount = fare + fee
    print("Passenger Fare: Rs.", amount)
    total = total + amount

print("\nTotal Fare: Rs.", total)

choice = input("Cancel ticket? (yes/no): ")

if choice == "yes":
    penalty = total * 0.25
    print("Cancellation Penalty: Rs.", penalty)
    print("Refund: Rs.", total - penalty)
else:
    print("Reservation Confirmed!")
