# Candlestick Chart

# Create a candlestick chart showing the movement of the BSE Sensex over the last 30 days. Read the data from a CSV file and display a candle for each trading day.

import pandas as pd
import mplfinance as mpl
sensex = pd.read_csv('sensex.csv').squeeze()
sensex["Date"] = pd.to_datetime(sensex["Date"])
sensex.set_index('Date', inplace=True)
mpl.plot(sensex,type='candle',title='BSE sensex',style='yahoo')