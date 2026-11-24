import csv
import matplotlib.pyplot as plt

departments = []
salaries = []
ids = []

with open("employees.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        departments.append(row["department"])
        salaries.append(int(row["salary"]))
        ids.append(int(row["id"]))

department_salaries = {}

for dept, salary in zip(departments, salaries):
    if dept not in department_salaries:
        department_salaries[dept] = []

    department_salaries[dept].append(salary)

avg_salary = {
    dept: sum(values) / len(values)
    for dept, values in department_salaries.items()
}

plt.figure(figsize=(8, 5))

bars = plt.bar(avg_salary.keys(), avg_salary.values(), color="skyblue")

plt.title("Average Salary per Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")

for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f"{bar.get_height():.0f}",
        ha="center",
        va="bottom"
    )

plt.tight_layout()
plt.savefig("bar_chart.png")
plt.close()

plt.figure(figsize=(8, 5))

plt.hist(salaries, bins=5, color="orange", edgecolor="black")

plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")

plt.tight_layout()
plt.savefig("histogram.png")
plt.close()

plt.figure(figsize=(8, 5))

colors = ["red", "blue", "green", "orange", "purple"]

unique_departments = list(set(departments))

for i, dept in enumerate(unique_departments):
    dept_ids = []
    dept_salaries = []

    for emp_id, salary, department in zip(ids, salaries, departments):
        if department == dept:
            dept_ids.append(emp_id)
            dept_salaries.append(salary)

    plt.scatter(
        dept_ids,
        dept_salaries,
        color=colors[i % len(colors)],
        label=dept
    )

plt.title("Employee ID vs Salary")
plt.xlabel("Employee ID")
plt.ylabel("Salary")
plt.legend()

plt.tight_layout()
plt.savefig("scatter_plot.png")
plt.close()

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [12, 15, 14, 18, 22, 25]

plt.figure(figsize=(8, 5))

plt.plot(
    months,
    sales,
    marker="o",
    color="green",
    linestyle="-",
    linewidth=2
)

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.tight_layout()
plt.savefig("line_chart.png")
plt.close()

print("All 4 charts created successfully!")
print("1. bar_chart.png")
print("2. histogram.png")
print("3. scatter_plot.png")
print("4. line_chart.png")