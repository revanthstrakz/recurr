import pandas as pd
import feather
import yfinance
import datetime
from datetime import date
import time
from IPython.display import clear_output
import os
def yf(df):
    tick=symbl+'.NS'
    x=yfinance.download(tick, interval='1m', period='7d')
    x=x.drop('Adj Close', axis=1)
    x['Datetime']=x.index
    df=df.append(x)
    return df

nse=pd.read_csv('ticker_data.csv')

def add(x):
    os.system('./script.sh')

for i,symbl in enumerate(nse.symbol):
#def lo(symbl):
    if i>-1:
        ipath = 'nse_stocks/{}.feather'.format(symbl)
        df=pd.read_feather(ipath)
        clear_output(wait=True)
        print(ipath, flush=True)
        #df=ini(df)
        df=yf(df)
        #return df
        feather.write_dataframe(df,ipath)
        path = '{}.feather'.format(symbl)
        add(path)
