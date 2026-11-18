import yfinance as yf
import pandas as pd

Ticker = "AAPL"

df = yf.download(Ticker, start="2021-01-01", end="2025-01-01")
print(df.head())