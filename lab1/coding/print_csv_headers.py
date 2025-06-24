# filename: print_csv_headers.py
import pandas as pd

# Load the data without setting an index
nvidia_data = pd.read_csv('nvidia_stock_data.csv')

# Print the columns of the dataframe
print("Column headers in the CSV file:")
print(nvidia_data.columns.tolist())