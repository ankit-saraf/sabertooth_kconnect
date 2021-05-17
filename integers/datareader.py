from pandas_datareader import data
# import pandas.io.data as web
import datetime

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2013, 1, 27)
f=data.DataReader("appl", 'yahoo', start, end)