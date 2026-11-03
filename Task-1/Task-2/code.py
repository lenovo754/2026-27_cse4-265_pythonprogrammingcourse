
# Progressive Electricity Billing System

FIXED_CHARGE = 50
SURCHARGE_RATE = 5
REBATE_RATE = 10
INCREASE_LIMIT = 30

bills = []

# Function to calculate energy charges
def calculate_energy_charges(units):

    if units <= 100:
        charge = units * 2

    elif units <= 200:
        charge = (100 * 2) + ((units - 100) * 3)

    elif units <= 300:
        charge = (100 * 2) + (100 * 3) + ((units - 200) * 5)

    else:
        charge = (100 * 2) + (100 * 3) + (100 * 5) + ((units - 300) * 7)

    return charge


# Input number of months
n = int(input("Enter number of months: "))

# Calculate monthly electricity bills
for i in range(n):

    print("\nEnter details for Month", i + 1)

    month = input("Enter month name: ")
    units = float(input("Enter electricity units consumed: "))

    if units < 0:
        print("Invalid units. Please enter a non-negative value.")
        continue

    # Calculate energy charges
    energy = calculate_energy_charges(units)

    # Calculate fixed charges
    fixed = FIXED_CHARGE

    # Calculate surcharge
    surcharge = energy * SURCHARGE_RATE / 100

    # Calculate rebate
    if units <= 100:
        rebate = energy * REBATE_RATE / 100
    else:
        rebate = 0

    # Calculate final bill
    total = energy + fixed + surcharge - rebate

    # Store monthly details
    bills.append({
        "month": month,
        "units": units,
        "energy": energy,
        "fixed": fixed,
        "surcharge": surcharge,
        "rebate": rebate,
        "total": total
    })


# Display monthly bills
print("\n========== ELECTRICITY BILL DETAILS ==========")

for bill in bills:

    print("\nMonth:", bill["month"])
    print("Units Consumed:", bill["units"])
    print("Energy Charges: Rs.", round(bill["energy"], 2))
    print("Fixed Charges: Rs.", bill["fixed"])
    print("Surcharge: Rs.", round(bill["surcharge"], 2))
    print("Rebate: Rs.", round(bill["rebate"], 2))
    print("Total Bill: Rs.", round(bill["total"], 2))


# Compare bills across months
print("\n========== MONTHLY BILL COMPARISON ==========")

for i in range(1, len(bills)):

    previous = bills[i - 1]["total"]
    current = bills[i]["total"]

    increase = current - previous

    if previous > 0:
        percentage = (increase / previous) * 100
    else:
        percentage = 0

    print("\n", bills[i]["month"], "vs", bills[i - 1]["month"])

    print("Previous Bill: Rs.", round(previous, 2))
    print("Current Bill: Rs.", round(current, 2))
    print("Change: Rs.", round(increase, 2))

    if increase > 0:
        print("Increase:", round(percentage, 2), "%")
    elif increase < 0:
        print("Decrease:", round(abs(percentage), 2), "%")
    else:
        print("No change in bill.")

    if previous > 0 and percentage > INCREASE_LIMIT:
        print("WARNING: Unusual increase detected!")
    else:
        print("Normal bill variation.")


print("\n========== BILLING SUMMARY ==========")

print("Total Months:", len(bills))

if bills:
    total_amount = sum(b["total"] for b in bills)
    average = total_amount / len(bills)

    print("Total Electricity Expense: Rs.", round(total_amount, 2))
    print("Average Monthly Bill: Rs.", round(average, 2))

print("\nBilling Process Completed.")

