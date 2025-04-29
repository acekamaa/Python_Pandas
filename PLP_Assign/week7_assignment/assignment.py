import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Task 1: Load and Explore the Dataset
try:
    # Load the Iris dataset
    iris = load_iris(as_frame=True)
    data = iris.frame
    print("✅ Dataset loaded successfully!\n")
except Exception as e:
    print(f"❌ Error loading dataset: {e}")

# Display the first few rows
print("🔹 First 5 Rows of the Dataset:")
print(data.head())

# Explore data types and missing values
print("\n🔹 Dataset Info:")
print(data.info())

print("\n🔹 Checking for missing values:")
print(data.isnull().sum())

# Clean dataset (Iris dataset has no missing values, but we'll show how you'd handle it)
data_cleaned = data.dropna()
print("\n✅ Cleaned dataset (if needed).")

# Task 2: Basic Data Analysis
# Compute basic statistics
print("\n🔹 Basic Statistics:")
print(data_cleaned.describe())

# Group by the species and compute mean of numerical columns
grouped = data_cleaned.groupby('target').mean()
print("\n🔹 Mean of each feature grouped by species (target):")
print(grouped)

# Optional: Map target numbers to species names for better clarity
target_names = dict(zip(range(3), iris.target_names))
data_cleaned['species'] = data_cleaned['target'].map(target_names)

# Identify patterns
print("\n🔹 Interesting Finding:")
most_sepal_length = data_cleaned.groupby('species')['sepal length (cm)'].mean().idxmax()
print(f"Species with the longest average sepal length: {most_sepal_length}")

# Task 3: Data Visualization
sns.set_style('whitegrid')  # Prettier plots

# 1. Line Chart: Trend of Sepal Length (just sorted index for illustration)
plt.figure(figsize=(10,6))
plt.plot(data_cleaned.index, data_cleaned['sepal length (cm)'], color='purple')
plt.title('Trend of Sepal Length (sorted index)')
plt.xlabel('Sample Index')
plt.ylabel('Sepal Length (cm)')
plt.grid(True)
plt.tight_layout()
plt.savefig('line_chart_sepal_length.png')
plt.show()

# 2. Bar Chart: Average Petal Length per Species
avg_petal_length = data_cleaned.groupby('species')['petal length (cm)'].mean()
plt.figure(figsize=(8,5))
avg_petal_length.plot(kind='bar', color=['skyblue', 'salmon', 'lightgreen'])
plt.title('Average Petal Length per Species')
plt.xlabel('Species')
plt.ylabel('Petal Length (cm)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('bar_chart_avg_petal_length.png')
plt.show()

# 3. Histogram: Distribution of Sepal Width
plt.figure(figsize=(8,5))
plt.hist(data_cleaned['sepal width (cm)'], bins=15, color='orange', edgecolor='black')
plt.title('Distribution of Sepal Width')
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('histogram_sepal_width.png')
plt.show()

# 4. Scatter Plot: Sepal Length vs Petal Length
plt.figure(figsize=(8,6))
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=data_cleaned, palette='Set2')
plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend(title='Species')
plt.tight_layout()
plt.savefig('scatter_sepal_vs_petal.png')
plt.show()
