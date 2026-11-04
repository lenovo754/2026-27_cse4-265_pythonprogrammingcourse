
# Manufacturing Cost and Profitability Analysis

try:
    print("MANUFACTURING COST AND PROFITABILITY ANALYSIS")

    # Input details
    product_name = input("\nEnter product name: ")

    quantity = int(input("Enter production quantity: "))

    material_cost = float(input("Enter material cost per unit: "))

    labour_cost = float(input("Enter labour charges per unit: "))

    wastage_rate = float(input("Enter wastage percentage: "))

    machine_cost = float(input("Enter total machine operating cost: "))

    selling_price = float(input("Enter selling price per unit: "))

    profit_target = float(input("Enter required profit target percentage: "))

    # Input validation
    if quantity <= 0:
        raise ValueError("Production quantity must be positive.")

    if material_cost < 0 or labour_cost < 0:
        raise ValueError("Material and labour costs cannot be negative.")

    if machine_cost < 0 or selling_price < 0:
        raise ValueError("Machine cost and selling price cannot be negative.")

    if not 0 <= wastage_rate <= 100:
        raise ValueError("Wastage percentage must be between 0 and 100.")

    if profit_target < 0:
        raise ValueError("Profit target cannot be negative.")

    # Cost calculations
    total_material_cost = material_cost * quantity

    total_labour_cost = labour_cost * quantity

    wastage_cost = total_material_cost * (wastage_rate / 100)

    total_manufacturing_cost = (
        total_material_cost
        + total_labour_cost
        + wastage_cost
        + machine_cost
    )

    cost_per_unit = total_manufacturing_cost / quantity

    # Revenue and profit calculations
    total_revenue = selling_price * quantity

    total_profit = total_revenue - total_manufacturing_cost

    profit_percentage = (
        (total_profit / total_manufacturing_cost) * 100
        if total_manufacturing_cost > 0
        else 0
    )

    # Profit target evaluation
    if profit_percentage >= profit_target:
        result = "PROFIT TARGET ACHIEVED"
    else:
        result = "PROFIT TARGET NOT ACHIEVED"

    # Display report
    print("\n" + "=" * 55)
    print("          MANUFACTURING COST REPORT")
    print("=" * 55)

    print("Product Name             :", product_name)
    print("Production Quantity      :", quantity)

    print("-" * 55)

    print(f"Total Material Cost      : Rs. {total_material_cost:.2f}")
    print(f"Total Labour Cost        : Rs. {total_labour_cost:.2f}")
    print(f"Wastage Cost             : Rs. {wastage_cost:.2f}")
    print(f"Machine Operating Cost   : Rs. {machine_cost:.2f}")

    print("-" * 55)

    print(f"Total Manufacturing Cost : Rs. {total_manufacturing_cost:.2f}")
    print(f"Manufacturing Cost/Unit  : Rs. {cost_per_unit:.2f}")
    print(f"Selling Price/Unit       : Rs. {selling_price:.2f}")
    print(f"Total Sales Revenue      : Rs. {total_revenue:.2f}")
    print(f"Total Profit             : Rs. {total_profit:.2f}")
    print(f"Profit Percentage        : {profit_percentage:.2f}%")
    print(f"Required Profit Target   : {profit_target:.2f}%")

    print("-" * 55)

    print("Profitability Status    :", result)

    print("=" * 55)

except ValueError as e:
    print("\nInput Error:", e)

