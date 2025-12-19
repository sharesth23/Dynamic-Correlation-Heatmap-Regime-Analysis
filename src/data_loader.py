import yfinance as yf
import pandas as pd

def load_data(tickers, start="2015-01-01"):
    data = {}

    for name, ticker in tickers.items():
        df = yf.download(ticker, start=start, progress=False)
        data[name] = df["Adj Close"]

    prices = pd.DataFrame(data)
    returns = prices.pct_change().dropna()

    return prices, returns
