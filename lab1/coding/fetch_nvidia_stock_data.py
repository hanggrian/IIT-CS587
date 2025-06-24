# filename: fetch_nvidia_stock_data.py
import yfinance as yf

# Ensure yfinance is installed, if not it is installed by this script
def install_package():
    import subprocess
    import sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "yfinance"])

try:
    import yfinance
except ImportError:
    install_package()
    import yfinance as yf

# Define the ticker symbol for Nvidia
nvidia_ticker = 'NVDA'

# Set the date range (past month)
start_date = '2024-03-23'
end_date = '2024-04-23'

# Fetch the historical data for Nvidia
nvidia_data = yf.download(nvidia_ticker, start=start_date, end=end_date)

# Save the data to a CSV file to review
nvidia_data.to_csv('nvidia_stock_data.csv')

# Print a preview of the data
print(nvidia_data.head())