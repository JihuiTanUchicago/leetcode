import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Generate mock data
symbols = ['AAPL', 'GOOG', 'TSLA', 'AMZN', 'MSFT', 'NVDA', 'META', 'NFLX', 'BABA', 'INTC']
start_date = datetime(2022, 1, 1)
num_days = 365 * 2  # 2 years of data
data = []

for i in range(num_days):
    date = start_date + timedelta(days=i)
    if date.weekday() >= 5:  # Skip weekends
        continue
    for symbol in symbols:
        if random.random() < 0.01:
            close_price = None  # Introduce some missing values
        else:
            base_price = 100 + symbols.index(symbol) * 50
            noise = np.random.normal(loc=0, scale=5)
            close_price = round(base_price + noise, 2)
        data.append([date.strftime('%Y-%m-%d'), symbol, close_price])

# Create DataFrame
df = pd.DataFrame(data, columns=['date', 'symbol', 'close'])

# Introduce some invalid symbols and bad data
for _ in range(20):
    idx = random.randint(0, len(df) - 1)
    df.at[idx, 'symbol'] = 'bad$symbol'
for _ in range(20):
    idx = random.randint(0, len(df) - 1)
    df.at[idx, 'close'] = -abs(df.at[idx, 'close'])  # negative close price

# Save to CSV
csv_path = "./stock_prices_mock.csv"
df.to_csv(csv_path, index=False)

csv_path
