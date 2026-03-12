import sqlite3
import pandas as pd
import random

conn = sqlite3.connect("employees.db")
cursor = conn.cursor()

# Query 1: 
query1 = """
SELECT name, department, salary, performance_score
FROM employees
WHERE performance_score >= 4.0 AND years_experience >= 3
ORDER BY performance_score DESC
LIMIT 15;
"""
df1 = pd.read_sql(query1, conn)
print("\nQuery 1 Results:\n", df1)

# Query 2
query2 = """
SELECT *
FROM employees
WHERE salary BETWEEN 70000 AND 110000
AND department IN ('Engineering','Sales')
ORDER BY department, salary DESC;
"""
df2 = pd.read_sql(query2, conn)
print("\nQuery 2 Results:\n", df2)

# Query 3
query3 = """
SELECT department, COUNT(*) AS emp_count, ROUND(AVG(salary),2) AS avg_salary
FROM employees
GROUP BY department
ORDER BY avg_salary DESC;
"""
df3 = pd.read_sql(query3, conn)
print("\nQuery 3 Results:\n", df3)
