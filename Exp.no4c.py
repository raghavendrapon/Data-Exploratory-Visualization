import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
sns.set_theme(style="whitegrid")

plt.figure(figsize=(6, 4))
sns.scatterplot(x="total_bill", y="tip", hue="sex", data=tips)
plt.title("Scatter Plot: Total Bill vs Tip")
plt.show()

plt.figure(figsize=(6, 4))
sns.boxplot(x="day", y="total_bill", data=tips, palette="pastel")
plt.title("Box Plot: Total Bill per Day")
plt.show()

plt.figure(figsize=(6, 4))
sns.violinplot(x="time", y="tip", data=tips, palette="muted")
plt.title("Violin Plot: Tip Amount by Time of Day")
plt.show()

