
# University Scholarship Allocation System

students = []
eligible_students = []

# Scholarship eligibility criteria
MIN_AGGREGATE = 75
MIN_SUBJECT_MARK = 50
MIN_ATTENDANCE = 75
MAX_INCOME = 300000

n = int(input("Enter number of students: "))

# Input student details
for i in range(n):
    print("\nEnter details of Student", i + 1)

    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")

    marks = []
    subjects = int(input("Enter number of subjects: "))

    for j in range(subjects):
        mark = float(input(f"Enter marks in subject {j + 1}: "))
        marks.append(mark)

    attendance = float(input("Enter attendance percentage: "))
    income = float(input("Enter annual family income: "))

    aggregate = sum(marks) / subjects

    student = {
        "name": name,
        "roll_no": roll_no,
        "aggregate": aggregate,
        "attendance": attendance,
        "income": income,
        "application_order": i + 1
    }

    students.append(student)

    # Check eligibility
    if (aggregate >= MIN_AGGREGATE and
        all(mark >= MIN_SUBJECT_MARK for mark in marks) and
        attendance >= MIN_ATTENDANCE and
        income <= MAX_INCOME):

        eligible_students.append(student)

# Sort eligible students
eligible_students.sort(
    key=lambda x: (
        -x["aggregate"],
        -x["attendance"],
        x["income"],
        x["application_order"]
    )
)

# Display results
print("\n===== SCHOLARSHIP ELIGIBILITY RESULTS =====")

if eligible_students:
    print("\nEligible Students Ranked by Merit:\n")

    for rank, student in enumerate(eligible_students, 1):
        print("Rank:", rank)
        print("Name:", student["name"])
        print("Roll Number:", student["roll_no"])
        print("Aggregate:", round(student["aggregate"], 2), "%")
        print("Attendance:", student["attendance"], "%")
        print("Family Income: Rs.", student["income"])
        print("--------------------------------")

else:
    print("No students are eligible for the scholarship.")

print("\nTotal Students:", n)
print("Eligible Students:", len(eligible_students))
print("Not Eligible Students:", n - len(eligible_students))

