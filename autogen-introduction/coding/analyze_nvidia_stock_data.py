# filename: analyze_nvidia_stock_data.py
import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file - adjusting column indexing
nvidia_data = pd.read_csv('nvidia_stock_data.csv')
nvidia_data['Date'] = pd.to_datetime(nvidia_data['Date'])
nvidia_data.set_index('Date', inplace=True)

# Calculate statistical details
max_price = nvidia_data['High'].max()
min_price = nvidia_data['Low'].min()
avg_price = nvidia_data['Close'].mean()

# Display the computed statistics
print("Maximum (High) price: ${:.2f}".format(max_price))
print("Minimum (Low) price: ${:.2f}".format(min_price))
print("Average (Close) price: ${:.2f}".format(avg_price))

# Identify significant changes
significant_changes = nvidia_data[
    nvidia_data['Volume'] > nvidia_data['Volume'].mean() + 1.5 * nvidia_data['Volume'].std()
]
print("Days with significant trading volume changes:")
print(significant_changes[['Volume']])

# Plot the closing prices
plt.figure(figsize=(10, 5))
plt.plot(nvidia_data['Close'], marker='o', linestyle='-', color='b')
plt.title('Nvidia Closing Stock Prices for the Past Month')
plt.xlabel('Date')
plt.ylabel('Closing Price ($)')
plt.grid(True)
plt.show()