
# Railway Fare and Reservation Calculator

# Function to calculate distance-based fare
def calculate_base_fare(distance):

    if distance <= 100:
        fare = distance * 1.50

    elif distance <= 300:
        fare = (100 * 1.50) + ((distance - 100) * 1.30)

    else:
        fare = (
            (100 * 1.50)
            + (200 * 1.30)
            + ((distance - 300) * 1.10)
        )

    return fare


# Function to calculate age concession
def calculate_concession(age, fare):

    if age < 5:
        concession = fare

    elif age <= 11:
        concession = fare * 0.50

    elif age >= 60:
        concession = fare * 0.40

    else:
        concession = 0

    return concession


# Function to calculate cancellation penalty
def calculate_cancellation_penalty(fare, hours):

    if hours > 48:
        rate = 0.10

    elif hours >= 12:
        rate = 0.25

    else:
        rate = 0.50

    return fare * rate


# Available travel classes
classes = {
    "1": ("Sleeper", 1.0),
    "2": ("AC 3 Tier", 2.0),
    "3": ("AC 2 Tier", 3.0),
    "4": ("AC First Class", 4.0)
}


# Main program
try:

    print("RAILWAY FARE AND RESERVATION CALCULATOR")

    n = int(input("\nEnter number of passengers: "))

    if n <= 0:
        raise ValueError("Number of passengers must be positive.")

    total_collection = 0
    total_refund = 0

    for i in range(n):

        print("\nPassenger", i + 1)
        print("-" * 45)

        name = input("Passenger Name: ").strip()
        age = int(input("Passenger Age: "))
        distance = float(input("Travel Distance (KM): "))

        if not name:
            raise ValueError("Passenger name cannot be empty.")

        if age < 0 or distance <= 0:
            raise ValueError("Invalid age or distance.")

        print("\nTravel Classes:")
        print("1. Sleeper")
        print("2. AC 3 Tier")
        print("3. AC 2 Tier")
        print("4. AC First Class")

        choice = input("Select Travel Class: ")

        if choice not in classes:
            raise ValueError("Invalid travel class.")

        class_name, multiplier = classes[choice]

        # Calculate basic fare
        base_fare = calculate_base_fare(distance)

        # Apply class multiplier
        class_fare = base_fare * multiplier

        # Calculate age concession
        concession = calculate_concession(
            age, class_fare
        )

        # Reservation charge
        reservation_fee = 40

        # Calculate final fare
        final_fare = (
            class_fare - concession + reservation_fee
        )

        total_collection += final_fare

        # Display fare statement
        print("\n" + "=" * 50)
        print("          RAILWAY FARE STATEMENT")
        print("=" * 50)

        print("Passenger Name :", name)
        print("Passenger Age  :", age)
        print("Distance       :", distance, "KM")
        print("Travel Class   :", class_name)

        print("-" * 50)

        print(f"Basic Fare     : Rs. {base_fare:.2f}")
        print(f"Class Fare     : Rs. {class_fare:.2f}")
        print(f"Concession     : Rs. {concession:.2f}")
        print(f"Reservation Fee: Rs. {reservation_fee:.2f}")

        print("-" * 50)

        print(f"TOTAL FARE     : Rs. {final_fare:.2f}")

        print("=" * 50)

        # Cancellation details
        cancel = input(
            "\nCancel ticket? (yes/no): "
        ).lower().strip()

        if cancel == "yes":

            hours = float(
                input("Hours before departure: ")
            )

            if hours < 0:
                raise ValueError(
                    "Cancellation hours cannot be negative."
                )

            penalty = calculate_cancellation_penalty(
                final_fare, hours
            )

            refund = final_fare - penalty

            total_refund += refund
            total_collection -= final_fare

            print("\nCANCELLATION STATEMENT")
            print("-" * 40)

            print(f"Ticket Fare : Rs. {final_fare:.2f}")
            print(f"Penalty     : Rs. {penalty:.2f}")
            print(f"Refund      : Rs. {refund:.2f}")

        elif cancel != "no":

            raise ValueError(
                "Enter yes or no for cancellation."
            )

    # Display final summary
    print("\n" + "=" * 50)
    print("             RAILWAY SUMMARY")
    print("=" * 50)

    print("Total Passengers :", n)
    print(f"Total Refunds    : Rs. {total_refund:.2f}")
    print(f"Net Revenue      : Rs. {total_collection:.2f}")

    print("=" * 50)

except ValueError as e:

    print("Input Error:", e)

