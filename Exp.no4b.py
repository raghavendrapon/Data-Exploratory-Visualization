import pandas as pd

df = pd.read_csv("C:\\Users\\ragha\\Downloads\\corporate_work_hours_productivity.csv")
df.columns = df.columns.str.strip()

df = df.dropna(subset=['Department', 'Monthly_Hours_Worked'])
df['Monthly_Hours_Worked'] = pd.to_numeric(df['Monthly_Hours_Worked'], errors='coerce')
df = df.dropna(subset=['Monthly_Hours_Worked'])

dept_hours = df.groupby('Department')['Monthly_Hours_Worked'].sum().reset_index()

pivot_table = dept_hours.pivot_table(values='Monthly_Hours_Worked', index='Department')

max_dept = pivot_table['Monthly_Hours_Worked'].idxmax()
max_hours = pivot_table['Monthly_Hours_Worked'].max()

print("\n📊 Department-wise Total Monthly Working Hours Summary:\n")
print(pivot_table)

print(f"\n🏆 Highest Total Working Hours:\n{max_dept} → {max_hours:.2f} hours")
