import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("Diabetes_Data.csv")
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date')

time = df['Date']
feature1 = df['BMI']
feature2 = df['Diabetes_Pedigree']

peaks1 = feature1[(feature1 > feature1.mean() + 2 * feature1.std())]
peaks2 = feature2[(feature2 > feature2.mean() + 2 * feature2.std())]

fig, ax = plt.subplots(figsize=(10, 6))
ax.set_title("BMI to Diabetes Comparison", fontsize=16)
ax.set_xlabel("Time", fontsize=12)
ax.set_ylabel("X", fontsize=12)
ax.set_xlim(time.min(), time.max())
ax.set_ylim(min(feature1.min(), feature2.min()), max(feature1.max(), feature2.max()))

ax.plot(time, feature1, label='BMI', color='blue', linewidth=1.5)
ax.plot(time, feature2, label='Diabetes_Pedigree', color='orange', linewidth=1.5)

ax.scatter(time.loc[peaks1.index], peaks1, color='red', label='Outliers (BMI)', s=50)
ax.scatter(time.loc[peaks2.index], peaks2, color='purple', label='Outliers (Diabetes_Pedigree)', s=50)

ax.legend(fontsize=12)

plt.tight_layout()
plt.show()
