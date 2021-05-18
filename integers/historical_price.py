from datetime import date
from nsepy import get_history


def history_data(symbol, start, end):
    s = start.split(',')
    e = end.split(',')
    data = get_history(symbol=symbol,
                    start=date(int(s[0]), int(s[1]), int(s[2])),
                    end=date(int(e[0]), int(e[1]), int(e[2])))
    
    return data

print(history_data('IRFC', "2021,1,1", "2021,1,15" ))
