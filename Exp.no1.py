import pandas as pd
import matplotlib.pyplot as plt

# Sample hardcoded data
data = {
    'Category': ['A', 'B', 'A', 'B', 'C'],
    'Value': [10, 15, 20, 25, 30]
}

# Create DataFrame from dictionary
df = pd.DataFrame(data)

# Show the DataFrame
print("Data:")
print(df)

# Group by 'Category' and calculate average
avg_values = df.groupby('Category')['Value'].mean()

# Plot a bar chart
avg_values.plot(kind='bar', color='green')
plt.title('Average Value per Category')
plt.xlabel('Category')
plt.ylabel('Average Value')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
