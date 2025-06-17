
import pandas as pd

# Load the dataset
df = pd.read_csv("C:\\Users\\ragha\\Downloads\\temperature.csv")

# Drop rows with invalid temperature
df = df[df['AvgTemperature'] != -99]

# Combine Year, Month, and Day into a single Date column
df['Date'] = pd.to_datetime(df[['Year', 'Month', 'Day']], errors='coerce')

# Drop rows with invalid dates (e.g., Feb 30)
df = df.dropna(subset=['Date'])

# Optional: Filter by Country or Year to reduce data
# df = df[df['Country'] == 'India']
# df = df[df['Year'] == 2020]

# Extract month name for pivoting
df['Month'] = df['Date'].dt.month_name()

# Group by City and Month, summing temperature
grouped = df.groupby(['City', 'Month'])['AvgTemperature'].sum().reset_index()

# Pivot the result to get month-wise temperature summary
pivot_table = grouped.pivot(index='City', columns='Month', values='AvgTemperature').fillna(0)

# Add a column for total temperature
pivot_table['Total'] = pivot_table.sum(axis=1)

# Print the table
print("Month-wise Temperature Summary:")
print(pivot_table)

# Identify city with highest total temperature
max_city = pivot_table['Total'].idxmax()
max_temp = pivot_table['Total'].max()

print(f"\nCity with highest total temperature: {max_city} ({max_temp:.2f}°F)")
