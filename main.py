
import json
import csv
import os

# Read JSON data
with open("data/employees.json", "r", encoding="utf-8") as file:
    json_data = json.load(file)

json_employees = json_data["employees"]

# Read CSV data
csv_employees = []

with open("data/employees.csv", "r", encoding="utf-8-sig", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        row = {k.strip(): v.strip() for k, v in row.items() if k}

        csv_employees.append({
            "id": int(row["id"]),
            "name": row["name"],
            "department": row["department"],
            "salary": int(row["salary"]),
            "active": row["active"].lower() == "true"
        })

# Combine JSON and CSV records
all_employees = json_employees + csv_employees

# Filter active employees
active_employees = [
    emp for emp in all_employees if emp["active"]
]

# Transform records
filtered_employees = []

for emp in active_employees:
    filtered_employees.append({
        "id": emp["id"],
        "name": emp["name"],
        "department": emp["department"],
        "salary": emp["salary"]
    })

# Calculate summary
total = len(filtered_employees)

average_salary = (
    sum(emp["salary"] for emp in filtered_employees) / total
    if total else 0
)

# Department summary
department_summary = {}

for emp in filtered_employees:
    dept = emp["department"]
    department_summary[dept] = department_summary.get(dept, 0) + 1

# Create audit report
summary = {
    "total_active_employees": total,
    "average_salary": average_salary,
    "department_summary": department_summary,
    "employees": filtered_employees
}

os.makedirs("output", exist_ok=True)

with open("output/summary_audit.json", "w", encoding="utf-8") as file:
    json.dump(summary, file, indent=4)

print("Data filtering completed successfully!")
print("Total active employees:", total)
print("Average salary:", average_salary)
print("Department summary:", department_summary)
print("Audit report saved successfully!")
