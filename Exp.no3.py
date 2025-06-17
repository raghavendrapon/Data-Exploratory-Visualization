import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
print("NumPy Operations:")

arr = np.array([10, 20, 30, 40, 50])
print("Original array:", arr)

print("Array + 5:", arr + 5)
print("Array squared:", arr ** 2)

print("\nPandas DataFrame Operations:")

data = {
    'Name': ['rohith', 'ragha', 'nithish', 'pavii','nive'],
    'Math': [99, 99, 98, 92,97],
    'Science': [88, 76, 93, 85,89]
}

df = pd.DataFrame(data)

print("\nDataFrame:")
print(df)

df['Average'] = (df['Math'] + df['Science']) / 2
print("\nWith Average Column:")
print(df)


print("\nGenerating Plots...")

plt.figure(figsize=(8, 4))
plt.bar(df['Name'], df['Math'], color='blue')
plt.title("Math Scores")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

plt.figure(figsize=(8, 4))
plt.plot(df['Name'], df['Math'], marker='o', label='Math')
plt.plot(df['Name'], df['Science'], marker='s', label='Science')
plt.title("Scores in Math and Science")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.legend()
plt.grid(True)
plt.show()
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
print("NumPy Operations:")

arr = np.array([10, 20, 30, 40, 50])
print("Original array:", arr)

print("Array + 5:", arr + 5)
print("Array squared:", arr ** 2)

print("\nPandas DataFrame Operations:")

data = {
    'Name': ['rohith', 'ragha', 'nithish', 'pavii','nive'],
    'Math': [99, 99, 98, 92,97],
    'Science': [88, 76, 93, 85,89]
}

df = pd.DataFrame(data)

print("\nDataFrame:")
print(df)

df['Average'] = (df['Math'] + df['Science']) / 2
print("\nWith Average Column:")
print(df)


print("\nGenerating Plots...")

plt.figure(figsize=(8, 4))
plt.bar(df['Name'], df['Math'], color='blue')
plt.title("Math Scores")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

plt.figure(figsize=(8, 4))
plt.plot(df['Name'], df['Math'], marker='o', label='Math')
plt.plot(df['Name'], df['Science'], marker='s', label='Science')
plt.title("Scores in Math and Science")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.legend()
plt.grid(True)
plt.show()
