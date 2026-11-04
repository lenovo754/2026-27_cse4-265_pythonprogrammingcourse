
import math

print("========================================")
print("   CAMPUS EVENT FINANCIAL PLANNING")
print("========================================")

# Input details
participants = int(input("Enter expected number of participants: "))

venue = float(input("Enter venue cost: Rs. "))
equipment = float(input("Enter equipment cost: Rs. "))
catering = float(input("Enter catering cost per participant: Rs. "))
transport = float(input("Enter transportation cost: Rs. "))
certificate = float(input("Enter certificate cost per participant: Rs. "))
sponsorship = float(input("Enter total sponsorship amount: Rs. "))

# Validate inputs
if participants <= 0:
    print("Error: Participants must be greater than zero.")

elif min(venue, equipment, catering, transport,
         certificate, sponsorship) < 0:
    print("Error: Costs and sponsorship cannot be negative.")

else:
    # Calculate fixed and variable costs
    fixed_cost = venue + equipment + transport
    variable_cost = catering + certificate

    # Calculate total expenses
    total_variable_cost = variable_cost * participants
    total_expenses = fixed_cost + total_variable_cost

    # Calculate sponsorship shortfall
    shortfall = max(0, total_expenses - sponsorship)

    # Calculate participant contribution
    fixed_shortfall = max(0, fixed_cost - sponsorship)

    contribution = (
        variable_cost + fixed_shortfall / participants
    )

    # Calculate break-even registrations
    if fixed_shortfall == 0:
        break_even = 1
    else:
        break_even = math.ceil(
            fixed_shortfall / (contribution - variable_cost)
        )

    # Display financial report
    print("\n========== FINANCIAL REPORT ==========")

    print(f"Expected Participants : {participants}")
    print(f"Venue Cost            : Rs. {venue:.2f}")
    print(f"Equipment Cost        : Rs. {equipment:.2f}")
    print(f"Catering Cost         : Rs. {total_variable_cost:.2f}")
    print(f"Transport Cost        : Rs. {transport:.2f}")
    print(f"Certificate Cost      : Rs. {certificate * participants:.2f}")

    print("-------------------------------------")
    print(f"Fixed Cost            : Rs. {fixed_cost:.2f}")
    print(f"Variable Cost         : Rs. {total_variable_cost:.2f}")
    print(f"Total Expenses        : Rs. {total_expenses:.2f}")
    print(f"Sponsorship           : Rs. {sponsorship:.2f}")
    print(f"Sponsorship Shortfall : Rs. {shortfall:.2f}")

    print("-------------------------------------")
    print(f"Contribution Per Person: Rs. {contribution:.2f}")
    print(f"Break-even Registrations: {break_even}")

    print("=====================================")
    print("       END OF FINANCIAL REPORT")
    print("=====================================")

