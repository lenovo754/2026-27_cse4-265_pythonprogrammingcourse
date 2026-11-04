
# Retail Billing with Multiple Discount Rules

tax_rates = {
    "electronics": 0.18,
    "clothing": 0.05,
    "grocery": 0.00,
    "furniture": 0.12
}

MAX_DISCOUNT = 2000


def calculate_discount(subtotal):

    if subtotal >= 10000:
        rate = 0.15
    elif subtotal >= 5000:
        rate = 0.10
    elif subtotal >= 1000:
        rate = 0.05
    else:
        rate = 0.00

    discount = subtotal * rate

    discount = min(discount, MAX_DISCOUNT)

    return discount, rate


try:
    print("RETAIL BILLING SYSTEM")

    n = int(input("\nEnter number of products: "))

    if n <= 0:
        raise ValueError("Number of products must be positive.")

    products = []

    total_subtotal = 0
    total_tax = 0

    for i in range(n):

        print(f"\nEnter details of Product {i + 1}")

        name = input("Product Name: ").strip()

        category = input(
            "Category (Electronics/Clothing/Grocery/Furniture): "
        ).lower().strip()

        quantity = int(input("Quantity: "))
        price = float(input("Unit Price: "))

        if not name:
            raise ValueError("Product name cannot be empty.")

        if category not in tax_rates:
            raise ValueError("Invalid product category.")

        if quantity <= 0 or price < 0:
            raise ValueError("Invalid quantity or price.")

        item_subtotal = quantity * price

        tax = item_subtotal * tax_rates[category]

        product = {
            "name": name,
            "category": category,
            "quantity": quantity,
            "price": price,
            "subtotal": item_subtotal,
            "tax": tax
        }

        products.append(product)

        total_subtotal += item_subtotal
        total_tax += tax

    discount, discount_rate = calculate_discount(total_subtotal)

    final_amount = total_subtotal + total_tax - discount

    print("\n" + "=" * 85)
    print("                         RETAIL INVOICE")
    print("=" * 85)

    print(
        f"{'Product':<18}"
        f"{'Category':<15}"
        f"{'Qty':>5}"
        f"{'Price':>12}"
        f"{'Subtotal':>13}"
        f"{'Tax':>10}"
    )

    print("-" * 85)

    for p in products:
        print(
            f"{p['name']:<18}"
            f"{p['category']:<15}"
            f"{p['quantity']:>5}"
            f"{p['price']:>12.2f}"
            f"{p['subtotal']:>13.2f}"
            f"{p['tax']:>10.2f}"
        )

    print("-" * 85)

    print(f"Total Subtotal       : Rs. {total_subtotal:.2f}")
    print(f"Total Category Tax   : Rs. {total_tax:.2f}")
    print(f"Discount Rate        : {discount_rate * 100:.0f}%")
    print(f"Discount Amount      : Rs. {discount:.2f}")
    print(f"Maximum Discount     : Rs. {MAX_DISCOUNT:.2f}")

    print("-" * 85)

    print(f"FINAL PAYABLE AMOUNT : Rs. {final_amount:.2f}")

    print("=" * 85)

except ValueError as e:
    print("Input Error:", e)

