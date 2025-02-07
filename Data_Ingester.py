import pandas as pd
import numpy as np
import datetime
import os
import yfinance as yf
from alpaca.data.historical import CryptoHistoricalDataClient
from alpaca.data.requests import CryptoBarsRequest
from alpaca.data.timeframe import TimeFrame


#domain = "https://paper-api.alpaca.markets/v2"

client = CryptoHistoricalDataClient()

request_params = CryptoBarsRequest(
    symbol_or_symbols=["BTC/USD"],
    timeframe=TimeFrame.Day,
    start="2022-09-01",
    end="2022-09-07",
)

btc_bars = client.get_crypto_bars(request_params)
print(btc_bars.df)