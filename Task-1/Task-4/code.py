
# Employee Payroll and Deduction Analysis

# Function to calculate progressive deductions
def calculate_deduction(gross_salary):

    deduction = 0

    slabs = [
        (10000, 0.00),
        (10000, 0.05),
        (30000, 0.10),
        (float('inf'), 0.15)
    ]

    remaining_salary = gross_salary

    for limit, rate in slabs:

        taxable_amount = min(remaining_salary, limit)

        deduction += taxable_amount * rate

        remaining_salary -= taxable_amount

        if remaining_salary <= 0:
            break

    return deduction


# Function to calculate salary
def calculate_salary(employee):

    gross_salary = (
        employee["basic"]
        + employee["allowances"]
        + employee["overtime"]
        + employee["incentives"]
    )

    deductions = calculate_deduction(gross_salary)

    net_salary = gross_salary - deductions

    return gross_salary, deductions, net_salary


# Function to display salary statement
def display_salary_statement(employee):

    gross, deduction, net = calculate_salary(employee)

    print("\n" + "=" * 55)
    print("          EMPLOYEE SALARY STATEMENT")
    print("=" * 55)

    print("Employee ID      :", employee["id"])
    print("Employee Name    :", employee["name"])

    print("-" * 55)

    print(f"Basic Pay        : Rs. {employee['basic']:,.2f}")
    print(f"Allowances       : Rs. {employee['allowances']:,.2f}")
    print(f"Overtime Payment : Rs. {employee['overtime']:,.2f}")
    print(f"Incentives       : Rs. {employee['incentives']:,.2f}")

    print("-" * 55)

    print(f"Gross Salary     : Rs. {gross:,.2f}")
    print(f"Total Deductions : Rs. {deduction:,.2f}")

    print("-" * 55)

    print(f"NET SALARY       : Rs. {net:,.2f}")

    print("=" * 55)


# Main program
employees = []

try:

    n = int(input("Enter number of employees: "))

    if n <= 0:
        raise ValueError("Number of employees must be positive.")

    for i in range(n):

        print(f"\nEnter details for Employee {i + 1}")

        emp_id = input("Employee ID: ").strip()
        name = input("Employee Name: ").strip()

        if not emp_id or not name:
            raise ValueError("Employee ID and name cannot be empty.")

        basic = float(input("Basic Pay: "))
        allowances = float(input("Allowances: "))
        overtime_hours = float(input("Overtime Hours: "))
        hourly_rate = float(input("Hourly Rate: "))
        incentives = float(input("Incentives: "))

        values = [
            basic, allowances, overtime_hours,
            hourly_rate, incentives
        ]

        if any(value < 0 for value in values):
            raise ValueError("Values cannot be negative.")

        overtime_payment = overtime_hours * hourly_rate

        employee = {
            "id": emp_id,
            "name": name,
            "basic": basic,
            "allowances": allowances,
            "overtime": overtime_payment,
            "incentives": incentives
        }

        employees.append(employee)

    # Payroll summary initialization
    total_gross = 0
    total_deductions = 0
    total_net = 0

    # Process employees
    for employee in employees:

        display_salary_statement(employee)

        gross, deduction, net = calculate_salary(employee)

        total_gross += gross
        total_deductions += deduction
        total_net += net

    # Calculate average salary
    average_salary = total_net / n

    # Display payroll summary
    print("\n" + "=" * 55)
    print("                 PAYROLL SUMMARY")
    print("=" * 55)

    print("Total Employees    :", n)
    print(f"Total Gross Salary : Rs. {total_gross:,.2f}")
    print(f"Total Deductions   : Rs. {total_deductions:,.2f}")
    print(f"Total Net Payroll  : Rs. {total_net:,.2f}")
    print(f"Average Net Salary : Rs. {average_salary:,.2f}")

    print("=" * 55)

except ValueError as e:

    print("Input Error:", e)

