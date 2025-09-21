import pandas as pd
import yfinance as yf
from cache_config import cache


TICKERS = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META', 'NVDA', 'TSLA', 'NFLX', 'INTC', 'AMD']
PERIODS = ['1mo', '3mo', '6mo', '1y', '5y', 'ytd', 'max']

@cache.memoize()
def get_ticker_data(ticker, period) -> pd.DataFrame:
    stock_df = yf.Ticker(ticker).history(period=period, interval='1d').reset_index()

    for col in stock_df.columns:
        if col == 'Date':
            stock_df['Date'] = pd.to_datetime(stock_df['Date']).dt.strftime('%Y-%m-%d')
        else:
            stock_df[col] = stock_df[col].round(2)
    
    return stock_df
