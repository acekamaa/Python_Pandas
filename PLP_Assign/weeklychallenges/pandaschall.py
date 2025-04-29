import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
data = pd.read_csv('/sales_data.csv')

# Calculate the total revenue
total_revenue = data['Revenue ($)'].sum()

# Find the best-selling product
best_selling = data.groupby('Product')['Quantity Sold'].sum().idxmax()
best_selling_quantity = data.groupby('Product')['Quantity Sold'].sum().max()

# Identify the day with the highest sales
highest_sales_day = data.groupby('Date')['Revenue ($)'].sum().idxmax()

# Save the results to a text file
with open('sales_summary.txt', 'w') as f:
    f.write(f"Total Revenue: ${total_revenue:,}\n")
    f.write(f"Best-Selling Product: {best_selling} ({best_selling_quantity} units sold)\n")
    f.write(f"Highest Sales Day: {highest_sales_day}\n")

# Print the insights in a user-friendly format
print(f"📊 Sales Summary:")
print(f"Total Revenue: ${total_revenue:,}")
print(f"Best-Selling Product: {best_selling} ({best_selling_quantity} units sold)")
print(f"Highest Sales Day: {highest_sales_day}")

# 🎯 Bonus: Visualize sales trends
# Group by date and sum the revenue
daily_sales = data.groupby('Date')['Revenue ($)'].sum()

# Plot the sales trend
plt.figure(figsize=(10, 6))
plt.plot(daily_sales.index, daily_sales.values, marker='o', linestyle='-', color='teal')
plt.title('Daily Sales Revenue Over Time')
plt.xlabel('Date')
plt.ylabel('Revenue ($)')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig('sales_trend.png')  # Save the plot as an image
plt.show()
