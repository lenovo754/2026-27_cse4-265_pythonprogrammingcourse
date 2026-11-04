
# Multi-Plan Telecommunications Cost Optimization

# Mobile plan details
plans = [
    {
        "name": "Basic Plan",
        "price": 199,
        "minutes": 200,
        "sms": 100,
        "data": 2,
        "validity": 28,
        "call_rate": 0.50,
        "sms_rate": 0.50,
        "data_rate": 20
    },
    {
        "name": "Standard Plan",
        "price": 399,
        "minutes": 500,
        "sms": 300,
        "data": 5,
        "validity": 56,
        "call_rate": 0.40,
        "sms_rate": 0.40,
        "data_rate": 15
    },
    {
        "name": "Premium Plan",
        "price": 599,
        "minutes": 1000,
        "sms": 500,
        "data": 10,
        "validity": 84,
        "call_rate": 0.30,
        "sms_rate": 0.30,
        "data_rate": 10
    },
    {
        "name": "Unlimited Plan",
        "price": 799,
        "minutes": 1500,
        "sms": 1000,
        "data": 20,
        "validity": 90,
        "call_rate": 0.20,
        "sms_rate": 0.20,
        "data_rate": 5
    }
]


# Function to calculate plan cost
def calculate_cost(plan, usage):

    excess_calls = max(
        0, usage["minutes"] - plan["minutes"]
    )

    excess_sms = max(
        0, usage["sms"] - plan["sms"]
    )

    excess_data = max(
        0, usage["data"] - plan["data"]
    )

    call_charge = excess_calls * plan["call_rate"]

    sms_charge = excess_sms * plan["sms_rate"]

    data_charge = excess_data * plan["data_rate"]

    excess_charge = (
        call_charge + sms_charge + data_charge
    )

    total_cost = plan["price"] + excess_charge

    return {
        "excess_calls": excess_calls,
        "excess_sms": excess_sms,
        "excess_data": excess_data,
        "call_charge": call_charge,
        "sms_charge": sms_charge,
        "data_charge": data_charge,
        "excess_charge": excess_charge,
        "total_cost": total_cost
    }


# Main program
try:

    print("MULTI-PLAN TELECOMMUNICATIONS COST OPTIMIZATION")

    print("\nEnter your monthly usage requirements")

    usage = {
        "minutes": float(input("Calling minutes: ")),
        "sms": int(input("Number of SMS: ")),
        "data": float(input("Data usage (GB): "))
    }

    required_validity = int(
        input("Required validity (days): ")
    )

    budget = float(input("Maximum budget (Rs.): "))

    if (
        any(value < 0 for value in usage.values())
        or required_validity <= 0
        or budget < 0
    ):
        raise ValueError("Inputs must be within valid ranges.")

    eligible_plans = []

    print("\n" + "=" * 75)
    print("                    MOBILE PLAN COMPARISON")
    print("=" * 75)

    print(
        f"{'Plan':<18}{'Base Price':>12}"
        f"{'Extra Cost':>13}{'Total Cost':>13}"
        f"{'Validity':>12}"
    )

    print("-" * 75)

    # Evaluate every plan
    for plan in plans:

        result = calculate_cost(plan, usage)

        total_cost = result["total_cost"]

        eligible = (
            plan["validity"] >= required_validity
            and total_cost <= budget
        )

        print(
            f"{plan['name']:<18}"
            f"{plan['price']:>12.2f}"
            f"{result['excess_charge']:>13.2f}"
            f"{total_cost:>13.2f}"
            f"{plan['validity']:>12}"
        )

        if eligible:
            eligible_plans.append({
                "plan": plan,
                "result": result
            })

    print("=" * 75)

    # Find the most economical eligible plan
    if eligible_plans:

        best = min(
            eligible_plans,
            key=lambda item: item["result"]["total_cost"]
        )

        plan = best["plan"]
        result = best["result"]

        print("\nMOST ECONOMICAL ELIGIBLE PLAN")
        print("-" * 45)

        print("Plan Name       :", plan["name"])
        print("Base Price      : Rs.", plan["price"])
        print("Excess Calls    :", result["excess_calls"])
        print("Excess SMS      :", result["excess_sms"])
        print("Excess Data     :", result["excess_data"], "GB")

        print("Call Charges    : Rs.",
              round(result["call_charge"], 2))

        print("SMS Charges     : Rs.",
              round(result["sms_charge"], 2))

        print("Data Charges    : Rs.",
              round(result["data_charge"], 2))

        print("Total Extra Cost: Rs.",
              round(result["excess_charge"], 2))

        print("TOTAL COST      : Rs.",
              round(result["total_cost"], 2))

        print("Validity        :", plan["validity"], "days")

        print("\nEligible Plans:", len(eligible_plans))

    else:

        print("\nNo eligible plan found.")

        print("Try increasing your budget or")
        print("reducing your usage requirements.")

except ValueError as e:

    print("Input Error:", e)

