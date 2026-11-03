
# Hospital Billing and Patient Classification System

patients = []

# Function to calculate concession
def calculate_concession(age, category):

    if category == "BPL":
        return 25

    elif age >= 60:
        return 15

    else:
        return 0


# Function to classify patients
def classify_patient(amount):

    if amount <= 5000:
        return "Low Payment"

    elif amount <= 20000:
        return "Medium Payment"

    else:
        return "High Payment"


# Input number of patients
n = int(input("Enter number of patients: "))

if n <= 0:
    print("Invalid number of patients.")

else:

    for i in range(n):

        print("\nEnter details of Patient", i + 1)

        patient_id = input("Enter Patient ID: ").strip()
        name = input("Enter Patient Name: ").strip()

        try:
            age = int(input("Enter Age: "))

            if age < 0 or age > 120:
                print("Invalid age. Patient record skipped.")
                continue

            category = input(
                "Enter Category (BPL/General): "
            ).strip().upper()

            if category not in ["BPL", "GENERAL"]:
                print("Invalid patient category.")
                continue

            consultation = float(
                input("Enter Consultation Charges: ")
            )

            diagnostic = float(
                input("Enter Diagnostic Charges: ")
            )

            treatment = float(
                input("Enter Treatment Charges: ")
            )

            # Validate charges
            if min(consultation, diagnostic, treatment) < 0:
                print("Invalid charges. Negative values not allowed.")
                continue

            if not patient_id or not name:
                print("Patient ID and name are required.")
                continue

        except ValueError:
            print("Invalid input. Please enter valid numeric values.")
            continue

        # Calculate total bill
        total = consultation + diagnostic + treatment

        # Calculate concession percentage
        discount_rate = calculate_concession(age, category)

        # Calculate concession amount
        concession = total * discount_rate / 100

        # Calculate final bill
        final_bill = total - concession

        # Classify patient
        classification = classify_patient(final_bill)

        # Store patient details
        patient = {
            "id": patient_id,
            "name": name,
            "age": age,
            "category": category,
            "total": total,
            "discount": concession,
            "final": final_bill,
            "classification": classification
        }

        patients.append(patient)

    # Display billing details
    print("\n========== HOSPITAL BILLING REPORT ==========")

    if not patients:
        print("No valid patient records available.")

    for patient in patients:

        print("\nPatient ID:", patient["id"])
        print("Patient Name:", patient["name"])
        print("Age:", patient["age"])
        print("Category:", patient["category"])

        print("Total Charges: Rs.",
              round(patient["total"], 2))

        print("Concession: Rs.",
              round(patient["discount"], 2))

        print("Final Bill: Rs.",
              round(patient["final"], 2))

        print("Patient Classification:",
              patient["classification"])

        print("-----------------------------------")

    # Summary
    if patients:

        total_patients = len(patients)

        total_revenue = sum(
            p["final"] for p in patients
        )

        print("\n========== BILLING SUMMARY ==========")

        print("Total Valid Patients:", total_patients)

        print("Total Hospital Revenue: Rs.",
              round(total_revenue, 2))

        print("Low Payment Patients:",
              sum(p["classification"] == "Low Payment"
                  for p in patients))

        print("Medium Payment Patients:",
              sum(p["classification"] == "Medium Payment"
                  for p in patients))

        print("High Payment Patients:",
              sum(p["classification"] == "High Payment"
                  for p in patients))

print("\nHospital Billing Process Completed.")

