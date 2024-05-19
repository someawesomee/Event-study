import json
import pandas as pd

import apimoex
import requests
from list_of_tickers import tickers


for stock in tickers:
    with requests.Session() as session:
        data = apimoex.get_board_history(session,security=stock, start='2021-02-01',end='2024-05-17', board='TQBR')
        
        df = pd.DataFrame(data)
        df['TICKER'] = stock
        # df['CAP'] = df['VOLUME'] * df['CLOSE']
        print(df.head())
        print(df.tail())
        print(df.info())
        df.to_csv('./stock_price.csv', mode='a', index=False)
