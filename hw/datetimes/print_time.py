import datetime
import datetime as dt

now = dt.datetime.now()

print(f'Today is {now.ctime()}; Number of week: {now.isocalendar()[1]}')

def datecron(days : int) -> datetime.date:
    date = dt.datetime.now()
    return date.replace(day=date.day + days)

print(datecron(2).ctime())