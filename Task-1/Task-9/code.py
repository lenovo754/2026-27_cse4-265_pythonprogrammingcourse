
# Multi-Currency Travel Budget Analysis

try:
    print("MULTI-CURRENCY TRAVEL BUDGET ANALYSIS")

    # Input basic details
    base_currency = input("\nEnter base currency (e.g. INR): ").upper()

    budget = float(input("Enter planned travel budget: "))

    fee_rate = float(input("Enter conversion fee percentage: "))

    n = int(input("Enter number of expense categories: "))

    # Input validation
    if not base_currency:
        raise ValueError("Base currency cannot be empty.")

    if budget <= 0:
        raise ValueError("Budget must be positive.")

    if fee_rate < 0 or fee_rate > 100:
        raise ValueError("Conversion fee must be between 0 and 100.")

    if n <= 0:
        raise ValueError("Number of expenses must be positive.")

    expenses = []
    total_spending = 0

    # Process each expense
    for i in range(n):

        print(f"\nExpense {i + 1}")

        category = input("Enter expense category: ").strip()

        amount = float(input("Enter expense amount: "))

        currency = input("Enter currency code: ").upper()

        exchange_rate = float(
            input(f"Enter exchange rate (1 {currency} in {base_currency}): ")
        )

        if not category:
            raise ValueError("Category cannot be empty.")

        if amount < 0 or exchange_rate <= 0:
            raise ValueError("Invalid amount or exchange rate.")

        # Currency conversion
        converted_amount = amount * exchange_rate

        # Calculate conversion fee
        conversion_fee = converted_amount * (fee_rate / 100)

        # Total expense including fee
        final_expense = converted_amount + conversion_fee

        expenses.append({
            "category": category,
            "currency": currency,
            "original_amount": amount,
            "converted_amount": converted_amount,
            "fee": conversion_fee,
            "total": final_expense
        })

        total_spending += final_expense

    # Find largest expense category
    largest_expense = max(expenses, key=lambda x: x["total"])

    # Budget comparison
    balance = budget - total_spending

    # Display report
    print("\n" + "=" * 85)
    print("             MULTI-CURRENCY TRAVEL BUDGET REPORT")
    print("=" * 85)

    print(f"Base Currency       : {base_currency}")
    print(f"Planned Budget      : {budget:.2f} {base_currency}")
    print(f"Conversion Fee Rate : {fee_rate:.2f}%")

    print("-" * 85)

    print(
        f"{'Category':<18}"
        f"{'Currency':<12}"
        f"{'Original':>12}"
        f"{'Converted':>14}"
        f"{'Fee':>12}"
        f"{'Total':>14}"
    )

    print("-" * 85)

    for e in expenses:
        print(
            f"{e['category']:<18}"
            f"{e['currency']:<12}"
            f"{e['original_amount']:>12.2f}"
            f"{e['converted_amount']:>14.2f}"
            f"{e['fee']:>12.2f}"
            f"{e['total']:>14.2f}"
        )

    print("-" * 85)

    print(
        f"Total Travel Spending : {total_spending:.2f} {base_currency}"
    )

    print(
        f"Largest Expense       : {largest_expense['category']}"
    )

    print(
        f"Largest Expense Amount: {largest_expense['total']:.2f} "
        f"{base_currency}"
    )

    if balance >= 0:
        print(f"Remaining Budget      : {balance:.2f} {base_currency}")
        print("Budget Status         : WITHIN BUDGET")
    else:
        print(f"Excess Spending       : {-balance:.2f} {base_currency}")
        print("Budget Status         : BUDGET EXCEEDED")

    print("=" * 85)

except ValueError as e:
    print("\nInput Error:", e)

