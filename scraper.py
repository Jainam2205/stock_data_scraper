import yfinance as yf
import pandas as pd
from datetime import datetime


def fetch_stock_data(ticker: str, start: str, end: str) -> pd.DataFrame:
    """
    Fetch historical daily stock data from Yahoo Finance.

    Args:
        ticker (str): Stock symbol, e.g., 'AAPL'.
        start (str): Start date in 'YYYY-MM-DD' format.
        end (str): End date in 'YYYY-MM-DD' format.

    Returns:
        pd.DataFrame: Stock data with Open, High, Low, Close, Volume, Adj Close.
    """
    try:
        data = yf.download(ticker, start=start, end=end)
        if data.empty:
            raise ValueError("No data found for ticker or date range.")
        return data
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        return pd.DataFrame()


def main():
    ticker = 'NVDA'
    start_date = '2024-01-01'
    end_date = datetime.today().strftime('%Y-%m-%d')

    print(f"Fetching data for {ticker} from {start_date} to {end_date}...")

    stock_data = fetch_stock_data(ticker, start_date, end_date)

    if not stock_data.empty:
        filename = f"{ticker}_stock_data_{start_date}_to_{end_date}.csv"
        stock_data.to_csv(filename)
        print(f"Data saved to {filename}")
    else:
        print("No data to save.")
if __name__ == '__main__':
    main()
