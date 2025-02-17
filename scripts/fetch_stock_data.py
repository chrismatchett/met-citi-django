import os
import sys
import django
# pip install yfinance
import yfinance as yf
from datetime import datetime, timedelta

# Add project root to Python path
sys.path.insert(0, 'C:\\Users\\chris\\Documents\\code\\met-citi-django')

# Set up Django environment
os.environ["DJANGO_SETTINGS_MODULE"] = "web_project.settings"
django.setup()

from hello.models import StockData  # Import your model

# Define the stock symbols
STOCKS = ["AAPL", "MSFT", "GOOGL"]

# Calculate date range (last year)
end_date = datetime.today().date()
start_date = end_date - timedelta(days=365)

# Fetch and save data
for stock in STOCKS:
    print(f"Fetching data for {stock}...")
    data = yf.download(stock, start=start_date, end=end_date)
    
    for date, row in data.iterrows():
        # Ensure no duplicate data
        if not StockData.objects.filter(symbol=stock, date=date).exists():
            StockData.objects.create(
                symbol=stock,
                date=date,
                open=row["Open"],
                high=row["High"],
                low=row["Low"],
                close=row["Close"],
                volume=row["Volume"]
            )
            print(f"Saved data for {stock} on {date}")
        else:
            print(f"Skipping {stock} on {date}, already exists.")
