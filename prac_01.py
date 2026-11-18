import yfinance as yf

TICKER = "AAPL"
START_DATE = "2021-01-01"
END_DATE = "2025-01-01"

prices = yf.download(
	TICKER,
	start=START_DATE,
	end=END_DATE,
	interval="1d",
	auto_adjust=False,
	progress=False,
	multi_level_index=False,
)

if prices.empty:
	raise RuntimeError(f"No price data returned for {TICKER}")

print(prices.head())