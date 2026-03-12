import sqlite3
import pandas as pd
import random

# Create connection
conn = sqlite3.connect("employees.db")
cursor = conn.cursor()

#Load all employees into Pandas
employees_df = pd.read_sql("SELECT * FROM employees", conn)

# Average performance score by department
avg_perf = employees_df.groupby("department")["performance_score"].mean()
print("\nAverage Performance Score by Department:\n", avg_perf)

# Replicate Query 1 using Pandas
query1_pandas = (
    employees_df.loc[(employees_df["performance_score"] >= 4.0) &
                     (employees_df["years_experience"] >= 3),
                     ["name", "department", "salary", "performance_score"]]
    .sort_values(by="performance_score", ascending=False)
    .head(15)
)
print("\nReplicated Query 1 in Pandas:\n", query1_pandas)
