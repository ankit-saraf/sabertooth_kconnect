import time
import datetime
import pandas as pd

code = 'TSLA'
period1 = int(time.mktime(datetime.datetime(2021, 4, 1, 23, 59).timetuple()))
period2 = int(time.mktime(datetime.datetime(2021, 4, 30, 23, 59).timetuple()))
interval = '1d'

query = f'https://query1.finance.yahoo.com/v7/finance/download/{code}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'

df = pd.read_csv(query)
print(df)