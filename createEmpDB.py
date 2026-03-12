import sqlite3
import random

# Create connection
conn = sqlite3.connect("employees.db")
cursor = conn.cursor()

# Drop table if exists
cursor.execute("DROP TABLE IF EXISTS employees")

# Create employees table
cursor.execute("""
CREATE TABLE employees (
    emp_id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary REAL,
    years_experience INTEGER,
    performance_score REAL
)
""")
print("Employee DataBase Created")

departments = ["Engineering", "Sales", "Marketing", "HR", "Finance"]

# Insert 40 synthetic records
for i in range(1, 41):
    name = f"Employee_{i}"
    department = random.choice(departments)
    salary = round(random.uniform(50000, 150000), 2)
    years_experience = random.randint(1, 15)
    performance_score = round(random.uniform(1.0, 5.0), 2)
    cursor.execute("INSERT INTO employees VALUES (?, ?, ?, ?, ?, ?)",
                   (i, name, department, salary, years_experience, performance_score))

# Count employees
cursor.execute("SELECT COUNT(*) FROM employees")
total_employees = cursor.fetchone()[0]
print("Total employees inserted:", total_employees)

# ✅ Commit before querying
conn.commit()

# Verify data
cursor.execute("SELECT * FROM employees")
employee_rows = cursor.fetchall()

# Print header
print(f"{'Emp_ID':<8}{'Name':<15}{'Department':<15}{'Salary':<12}{'Experience':<12}{'Perf_Score':<12}")

# Print each row with alignment
for emp_id, name, department, salary, years_experience, performance_score in employee_rows:
    print(f"{emp_id:<8}{name:<15}{department:<15}{salary:<12.2f}{years_experience:<12}{performance_score:<12.2f}")




conn.close()
